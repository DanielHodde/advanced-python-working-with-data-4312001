# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def get_sig(q):
    sig = q["properties"]["sig"]
    return 0 if sig is None else sig

most_sig = sorted(data["features"], key=get_sig, reverse=True)[0:40]
most_sig.sort(key=lambda e: e["properties"]["time"], reverse=True)

# print(most_sig)

header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
rows = []

for quake in most_sig:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"]/1000))
    coords = quake["geometry"]["coordinates"]
    link = f"https://www.google.com/maps/search/?api=1&query={coords[1]}%2C{coords[0]}"
    rows.append([quake["properties"]["mag"],
                quake["properties"]["place"],
                quake["properties"]["felt"],
                thedate,
                link])

with open("sigquakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
