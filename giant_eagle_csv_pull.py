import pandas as pd

df = pd.read_csv('./getgos_1.csv')

final = {}

store_nums = df["Store #"]
addresses = df["Address 1"]
cities = df["City"]
states = df["State"]
zips = df["Zip"]

for i in range(store_nums.size):
	final[str(store_nums[i])] = addresses[i] + ' ' + cities[i] + ', ' + states[i] + ' ' + zips[i]

ser = pd.Series(final)

ser.to_csv('GetGo_Locations1.csv')