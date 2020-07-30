'''
@file: run.py

@author: Rukmangadh Sai Myana
@mail: rukman.sai@gmail.com
'''


import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def assign_day_numbers(single_cohort):
    '''
    Given a cohort data frame, assign the day numbers.
    '''
    single_cohort['date'] = list(range(1, len(single_cohort)+1))
    single_cohort.rename(columns={'date': 'day'}, inplace=True)
    return single_cohort


if __name__ == '__main__':
    # ---------------------------- Program Flags -----------------------------#
    parser = argparse.ArgumentParser()
    parser.add_argument('--datafile', default='./search_cohort_raw.csv',
                        type=str, help='The path to the data file.')

    args = parser.parse_args()

    # ----------------------------- Import data ------------------------------#
    data = pd.read_csv(args.datafile)

    # -------------------------- Find Initial Visit --------------------------#
    # group data w.r.t user id
    data.set_index('user_id', inplace=True)
    user_grouped_data = data.groupby(by='user_id')
    first_visits = user_grouped_data['date'].min()

    # add first visits to the dataframe
    data['cohort'] = first_visits
    data.reset_index(inplace=True)
    data = data.reindex(columns=['cohort', 'date', 'user_id'])

    # ---------------------------- Build Cohorts -----------------------------#
    grouped_data = data.groupby(by=['cohort', 'date'])
    cohorted_data = grouped_data.aggregate(
        {'user_id': pd.Series.nunique})  # returns a dataframe
    cohorted_data.rename(columns={'user_id': 'user_count'}, inplace=True)

    # ------------------------ Convert to Table Form -------------------------#
    cohorted_data.reset_index(inplace=True)
    cohorted_data = cohorted_data.groupby(by='cohort')

    # assign appropriate day number w.r.t the cohort
    cohorted_data = cohorted_data.apply(
        assign_day_numbers)  # returns a dataframe
    cohorted_data.index = pd.MultiIndex.from_frame(
        cohorted_data[['cohort', 'day']])
    cohorted_data = cohorted_data[['user_count']]
    cohorted_data = cohorted_data.unstack(1)

    # ------------------------ Normalize the table ---------------------------#
    cohort_sizes = cohorted_data.loc[:, 'user_count'][1]
    normalized_table = cohorted_data['user_count'].div(
        cohort_sizes, axis=0)*100

    # ------------------------- Visualize the Data ---------------------------#
    sns.set(style='white')
    sns.heatmap(normalized_table, mask=normalized_table.isnull(),
                annot=True, fmt='.0f', cmap='Blues')
    plt.show()
