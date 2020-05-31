print("Hello World")
print(type(3))
ballots = 1,341
print(ballots)
print(type(ballots))
print(type(73.81))
print(type("Hello World"))
print(type(True))

print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5+(9*3/2-4))

counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
counties[0]
print(counties[0])
print(counties[1])
print(counties[2])
print(len(counties))
print(counties[0:2])
print(counties[0:1])

counties.append("El Paso")
counties.insert(2, "El Paso")
print(len(counties))
print(counties)

counties.remove("El Paso")
print(counties)

counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)

counties = ["Arapahoe", "Denver", "Jefferson"]
counties.append("El Paso")
counties.remove("Arapahoe")
counties.append("Denver")
counties.append("Jefferon")
counties.pop(0)
counties.pop(0)
counties.append("Arapahoe")
print(counties)


counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict["Arapahoe"])
print(counties_dict["Denver"])
print(counties_dict["Jefferson"])
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.get("Denver"))

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 46335})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.pop(0)
voting_data.pop(0)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)

count = 7
while count < 1:
    print("Hello World")

for county in counties:
    print(county)  

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county,"county has", voters, "registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
for data in voting_data:
    print(f'{data["county"]} county has {data["registered_voters"]} registered voters')

