# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:48:55 2018

@author: Data Monkey

inspired by https://github.com/paulgb/gtfs-gexf/blob/master/transform.py
"""

import networkx as nx
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from csv import DictReader
from itertools import groupby
import cartopy.feature as cfeature

    
DATA_ROOT='C:\\Users\\rolan\\Downloads\\SydneyTrains\\'

G = nx.Graph()

trips_csv = DictReader(open(f'{DATA_ROOT}trips.txt','r'))
stops_csv = DictReader(open(f'{DATA_ROOT}stops.txt','r'))
stop_times_csv = DictReader(open(f'{DATA_ROOT}stop_times.txt','r'))
routes_csv = DictReader(open(f'{DATA_ROOT}routes.txt','r'))


def get_stop_id(stop_id):
    if stop_details[stop_id]['parent_station'] == '':
        return stop_id
    else:
        return stop_details[stop_id]['parent_station']

def add_stop_to_graph(G, stop_id):
    node = stop_details[get_stop_id(stop_id)]
    G.add_node(node['stop_id'], 
               stop_name = node['stop_name'], 
               stop_lon = node['stop_lon'], 
               stop_lat = node['stop_lat'])

def add_edge_to_graph(G, from_id, to_id, color):
    G.add_edge(get_stop_id(from_id), get_stop_id(to_id), color=color)




routes = dict()
for route in routes_csv:
    #if route['route_type'] in CONVERT_ROUTE_TYPES:
    routes[route['route_id']] = route
print ('routes', len(routes))
    
trips = dict()
for trip in trips_csv:
    if trip['route_id'] in routes:
        trip['color'] = routes[trip['route_id']]['route_color']
        trips[trip['trip_id']] = trip
print ('trips', len(trips))

stop_details = dict()
for stop_iter in stops_csv:
    stop_details[stop_iter['stop_id']] = stop_iter
print ('stop_details', len(stop_details))   

stops = set()
edges = dict()
for trip_id, stop_time_iter in groupby(stop_times_csv, lambda stop_time: stop_time['trip_id']):
    if trip_id in trips:
        trip = trips[trip_id]
        prev_stop = next(stop_time_iter)['stop_id']
        stops.add(prev_stop)
        for stop_time in stop_time_iter:
            stop = stop_time['stop_id']
            edge = (prev_stop, stop)
            edges[edge] = trip['color']
            stops.add(stop)
            prev_stop = stop
print ('stops', len(stops))
print ('edges', len(edges))

for stop_id in stop_details:
    if stop_id in stops:
       add_stop_to_graph(G, stop_id)
print('Nodes:', G.number_of_nodes() )
        
for (start_stop_id, end_stop_id), color in edges.items():
    add_edge_to_graph(G, 
                      from_id = start_stop_id, 
                      to_id = end_stop_id, 
                      color=color)
print('Edges:', G.number_of_edges() )


deg = nx.degree(G)
labels = {stop_id: G.node[stop_id]['stop_name'] if deg[stop_id] >= 1 else ''
          for stop_id in G.nodes}

pos = {stop_id: (G.node[stop_id]['stop_lon'], G.node[stop_id]['stop_lat'])
       for stop_id in G.nodes}





fig = plt.figure(figsize=(20,20))
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=140))
#ax.set_extent((144, 155, -35, -32))

nx.draw_networkx(G, ax=ax
##,
                 ,labels=labels
                 ,pos=pos
                )
#ax.set_axis_off()

plt.show()
