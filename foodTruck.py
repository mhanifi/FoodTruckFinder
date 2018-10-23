import pandas as pd
import numpy as np
import os
import geocoder
from geopy.distance import geodesic
from flask import Flask, jsonify
import json


def findDistance(fromLocation, toLocation):
    return geodesic(myLocation, toLocation).km

currentDir = os.getcwd()

bigList = pd.read_csv(os.path.join(currentDir , "fullList/Mobile_Food_Facility_Permit.csv"))
setOfBigList = set(bigList["Applicant"].str.strip()+ bigList["FoodItems"].str.strip())


dumpList = pd.read_csv(os.path.join(currentDir, "dumpdata/Mobile_Food_Facility_Permit.csv"))
setOfDumpList = set(dumpList["Applicant"].str.strip()+ dumpList["FoodItems"].str.strip())

notVisitedYet = setOfBigList - setOfDumpList

g = geocoder.ip('me')
myLocation = g.latlng


bigList["TruckPlusFood"] = bigList["Applicant"] + bigList["FoodItems"]
fiveClosesetTrucks=bigList[bigList["TruckPlusFood"].isin(notVisitedYet)]
fiveClosesetTrucks["Distance"] = 0
for index, row in fiveClosesetTrucks.iterrows():
    fiveClosesetTrucks.loc[index, "Distance"] = (findDistance(myLocation,[row["Latitude"], row["Longitude"]]))


fiveClosesetTrucks = fiveClosesetTrucks.sort_values(by=['Distance']).iloc[0:4,:]
fiveClosesetTrucks = fiveClosesetTrucks.loc[:, ["Applicant", "LocationDescription", "Address", "FoodItems", "lot", "Latitude", "Longitude", "dayshours"]]
fiveClosesetTrucks = fiveClosesetTrucks.fillna("N/A")

fiveLatLongList= fiveClosesetTrucks[["Latitude","Longitude"]]

def latlong():
    return json.dumps(json.loads(fiveLatLongList.to_json(orient='table')), indent=4)

REQUEST = fiveClosesetTrucks.to_json( orient = 'table')


def index():
    return json.dumps(json.loads(REQUEST), indent=4)
