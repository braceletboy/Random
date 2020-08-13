'''
@file: run.py

Spatial Optimization

@author: Rukmangadh Sai Myana
@mail: rukman.sai@gmail.com
'''


import folium
import argparse
import pandas as pd
import numpy as np
import geopandas as gpd
from pyproj import CRS
from shapely.geometry import Point
from sklearn.neighbors import KernelDensity
from statsmodels.nonparametric.bandwidths import bw_silverman


def non_negative_float(flag_str):
    '''
    Convert the flag input to a float and raise error if the float is not
    non negative.

    @param flag_str: The flag input

    @returns: The float form of the input string
    '''
    value = float(flag_str)
    if value < 0:
        message = '{} is not a non negative float'.format(flag_str)
        raise argparse.ArgumentTypeError(message)
    return value


def get_bpoints(args):
    '''
    Get the best points in the datasets.

    @param args: The flag arguments given to the file.

    @returns: The best locations as a dataframe.
    '''
    # Load Data
    bus_stops_data = pd.read_csv(args.bus_stops_file)
    hospitals_data = pd.read_csv(args.hospitals_file)
    restaurants_data = pd.read_csv(args.restaurants_file)

    # Prepare Data
    bus_stops_data['weights'] = args.bus_stops_weight
    bus_stops_data['location_type'] = 'bus_stop'
    hospitals_data['weights'] = args.hospitals_weight
    hospitals_data['location_type'] = 'hospital'
    restaurants_data['weights'] = args.restaurants_weight
    restaurants_data['location_type'] = 'restaurant'
    datasets = [bus_stops_data, hospitals_data, restaurants_data]
    merged_data = pd.concat(datasets)
    weights = merged_data['weights']

    # Kernel Density Estimation
    silverman_bandwidth = max(bw_silverman(
        merged_data[['latitude', 'longitude']].to_numpy()))
    kde = KernelDensity(bandwidth=silverman_bandwidth,
                        algorithm='ball_tree', metric='haversine')
    trained_estimator = kde.fit(
        merged_data[['latitude', 'longitude']].to_numpy(), weights.to_numpy())

    # Finding Best Coordinates
    bpoint_indices = np.argsort(trained_estimator.score_samples(
        merged_data[['latitude', 'longitude']].to_numpy()))[-args.num_bpoints:]
    bpoint_indices = np.flip(bpoint_indices)  # order descendingly
    best_locations = merged_data.iloc[bpoint_indices]
    best_locations.index = range(1, 6)  # show the ranks of the locations
    return best_locations


def visualize(best_locations):
    '''
    Visulaize the given locations on a map.

    @param best_locations: The best locations given as a dataframe.
    '''
    # convert locations to points ('x' is longitude and 'y' is latitude)
    best_points = [Point(location) for location in zip(
        best_locations['longitude'], best_locations['latitude'])]

    # create a geo dataframe for ease of marking points on folium
    gdf = gpd.GeoDataFrame({
        'id': best_locations['id'].to_numpy(),
        'location_type': best_locations['location_type'].to_numpy(),
        'geometry': best_points
    })

    # set crs - coordinate reference system for the geo dataframe
    gdf.crs = CRS.from_epsg(4326)  # latitude longitude system

    # convert to mercator system because our map is a mercator map
    gdf.to_crs(CRS.from_epsg(3395), inplace=True)

    # map it
    map_plot = folium.Map(location=[
        np.mean(best_locations['latitude'].to_numpy()),
        np.mean(best_locations['longitude'].to_numpy())], zoom_start=14)
    points_gjson = folium.features.GeoJson(
        gdf['geometry'], name='best_locations')
    points_gjson.add_to(map_plot)
    map_plot.save('./bpoints.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # ------------------ Flags for configuring parameters ------------------- #
    parser.add_argument('--bus_stops_file', default='./bus_stops.csv',
                        type=str, help='The path to the bus stops data file.')
    parser.add_argument('--hospitals_file', default='./hospitals.csv',
                        type=str, help='The path to the bus stops data file.')
    parser.add_argument('--restaurants_file', default='./restaurants.csv',
                        type=str, help='The path to the bus stops data file.')
    parser.add_argument('--bus_stops_weight', default='0.5',
                        type=non_negative_float, help='The weight that the\
                        user has for a bus stop.')
    parser.add_argument('--hospitals_weight', default='1',
                        type=non_negative_float, help='The weight that the\
                        user has for a hospital.')
    parser.add_argument('--restaurants_weight', default='0.25',
                        type=non_negative_float, help='The weight that the\
                        user has for a restaurant.')
    parser.add_argument('--num_bpoints', default=5, type=int, help='The\
                        number of best points the user wants')

    args = parser.parse_args()

    best_locations = get_bpoints(args)  # get the best locations
    visualize(best_locations)  # Visualization
