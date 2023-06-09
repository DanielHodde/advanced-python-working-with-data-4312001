# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1:
total = len(data["features"])

# 2:
def more_hundo(q):
    if (q["properties"]["felt"] is not None) and \
          q["properties"]["felt"] >= 100:
        return True
    return False
hundo = len(list(filter(more_hundo, data["features"])))

#3:
def get_felt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0


max_felt = max(data['features'], key=get_felt)

#4:
def get_sig(q):
    return q["properties"]["sig"]

data["features"].sort(key=get_sig, reverse=True)

# Print all
print(f"Total quakes: {total}")
print(f"Total quakes felt by at least 100 people: {hundo}")
print(f"Most felt reports: {max_felt['properties']['title']},\
      reports: {max_felt['properties']['felt']}")
print("The 10 most significant events were:")
for i in range(0, 10):
    print(f"Event: {data['features'][i]['properties']['title']}, \
          Significance: {data['features'][i]['properties']['sig']}")
