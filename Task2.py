# -*- coding: utf-8 -*-
"""@author: marabetaniav
    Application with three different features: Jumps, Walks and distance 
    To collect the Data Set the App AndroSensor was used. 
    The user jumped and walked a considerable distance. In this application you
    will find out how was the total distance recorred by the user, how many
    steps did the user do and how many jumps did.
"""
import math
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import find_peaks

#Read the data neccesary for the application
#Extract the information from the Dataset 
DATA_FIELDL = pd.read_csv('Sensor_record_20181112_083240_AndroSensor.csv')
LATITUD = DATA_FIELDL['LOCATION Latitude : ']
LONGITUD = DATA_FIELDL['LOCATION Longitude : ']
LAT_1 = LATITUD[0]
LON_1 = LONGITUD[0]
LAT_2 = LATITUD[len(LATITUD)-1]
LON_2 = LONGITUD[len(LONGITUD)-1]
ACC_X = DATA_FIELDL['ACCELEROMETER X']
ACC_Y = DATA_FIELDL['ACCELEROMETER Y']
ACC_Z = DATA_FIELDL['ACCELEROMETER Z']
TIME = DATA_FIELDL['Time']
#Distances
def haversine(x_1, y_1, x_2, y_2):
    """
    distance
    """
# convert decimal degrees to radians
# x longitud y latitud
    x_1, y_1, x_2, y_2 = map(radians, [x_1, y_1, x_2, y_2])
# haversine formula
    d_lon = x_2 - x_1
    d_lat = y_2 - y_1
    a_d = sin(d_lat/2)**2 + cos(y_1) * cos(y_2) * sin(d_lon/2)**2
    c_d = 2 * asin(sqrt(a_d))
    r_d = 6371 # Radius of earth in kilometers. Use 3956 for miles
    dis_h = c_d*r_d
    return dis_h
#Steps and Jumps
def acceleration_xyz(a_x, a_y, a_z):
    """  accelaration  """
    acce = a_x ** 2 + a_y ** 2 + a_z ** 2
    acce = acce.apply(math.sqrt)  # magnitude of Acceleration
    acce = (acce - acce.mean())/acce.std()
    return acce
D = haversine(LON_1, LAT_1, LON_2, LAT_2)
ACC = acceleration_xyz(ACC_X, ACC_Y, ACC_Z)
#using find_peaks function, filterin signal
PEAKS_JUMPS, _ = find_peaks(ACC, height=(4.5, 6.2))#finding the peaks of jumps
PEAKS_STEPS, _ = find_peaks(ACC, height=(0.5, 3))#finding the peaks of steps
#ploting the signal
plt.figure(figsize=(10, 10))
plt.plot(ACC)
plt.plot(PEAKS_JUMPS, ACC[PEAKS_JUMPS], "x")
plt.plot(PEAKS_STEPS, ACC[PEAKS_STEPS], "x")
plt.plot(np.zeros_like(ACC), "--", color="gray")
plt.ylabel('Acceleration')
plt.show()
print("**Your Total Distance:%sKm"%D)
print("**Total Jumps:%s"%len(PEAKS_JUMPS))
print("**Total Steps:%s"%len(PEAKS_STEPS))
