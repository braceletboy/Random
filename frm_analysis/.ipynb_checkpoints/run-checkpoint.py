# Field Relationship Manager - Distance Travelled

import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt


def calculate_distance(dataframe):
    '''
    Calculate the distance.
    '''
    # sort the values by time
    dataframe.sort_values('time', inplace=True)

    # find coordinates of each chord in the path
    dataframe['end_lat'] = dataframe['start_lat'].shift(periods=-1)
    dataframe['end_long'] = dataframe['start_long'].shift(periods=-1)
    dataframe['end_lat'].iat[-1] = dataframe['start_lat'].iloc[-1]
    dataframe['end_long'].iat[-1] = dataframe['start_long'].iloc[-1]
    dataframe['diff_lat'] = (dataframe['start_lat'] - dataframe['end_lat'])/2
    dataframe['diff_long'] = (
        dataframe['start_long'] - dataframe['end_long'])/2

    # calculate the distance for each chord in the path
    earth_radius = 6371  # in kilometers
    dataframe['chord_distance'] = ((dataframe['diff_lat'].apply(np.sin))**2 +
                                   dataframe['start_lat'].apply(np.cos) *
                                   dataframe['end_lat'].apply(np.cos) *
                                   (dataframe['diff_long'].apply(np.sin))**2)
    dataframe['chord_distance'] = 2*earth_radius * \
        (dataframe['chord_distance'].apply(np.sqrt)).apply(np.arcsin)
    return dataframe


if __name__ == '__main__':
    # ---------------------------- Program Flags -----------------------------#
    parser = argparse.ArgumentParser()
    parser.add_argument('--datafile', default='./frm_locations.csv',
                        type=str, help='The path to the data file.')

    args = parser.parse_args()

    # ----------------------- Load and prepare Data --------------------------#
    frm_data = pd.read_csv(args.datafile)
    frm_data.rename(columns={'date': 'time_stamp', 'latitude': 'start_lat',
                             'longitude': 'start_long'}, inplace=True)
    frm_data['date'] = frm_data['time_stamp'].apply(lambda x: x[:10])
    frm_data['time'] = frm_data['time_stamp'].apply(lambda x: x[11:19])
    frm_data = frm_data.groupby(['frm_id', 'date'])

    # -------------------------- Calculate Distance --------------------------#
    frm_data = frm_data.apply(calculate_distance)  # returns dataframe
    frm_data.reset_index(drop=True, inplace=True)
    distance_dataframe = frm_data.loc[:, ['frm_id', 'date', 'chord_distance']]
    distance_dataframe.set_index(['frm_id', 'date'], inplace=True)

    # clean outliers
    upper_threshold = 10  # max movement is 10 kilometers
    lower_threshold = 0.001  # min movement is 1 meter
    distance_dataframe = distance_dataframe[distance_dataframe <=
                                            upper_threshold]
    distance_dataframe = distance_dataframe[distance_dataframe >=
                                            lower_threshold]

    # calculate total distance travelled
    distance_dataframe = distance_dataframe.groupby(by=['frm_id', 'date'])
    distance_dataframe = distance_dataframe.sum()  # returns dataframe
    distance_dataframe = distance_dataframe.unstack()['chord_distance']

    # ---------------------------- Visualization -----------------------------#
    fig, ax = plt.subplots()

    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    table = pd.plotting.table(ax, distance_dataframe, cellLoc='center',
                              rowLoc='center', colLoc='center', loc='center')
    table.set_fontsize(34)
    fig.tight_layout()
    plt.show()
