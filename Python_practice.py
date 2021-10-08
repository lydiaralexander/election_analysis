# counties = ["Arapahoe", "Denver", "Jefferson"]
# # # if "El Paso" in counties:
# # #     print("El Paso is in the list of counties.")
# # # else:
# # #     print("El Paso is not in the list of counties.")

# # if "Arapahoe" in counties and "El Paso" in counties:
# #     print("Arapahoe and El Paso are in  the list of counties")
# # else:
# #     print("Arapahoe or El Paso is not in the list counties")

# # # set the variable x = 0 before we enter the loop
# # x = 0
# # # we test if x is less than or equal to 5
# # while x <= 5:
# #     # if this condition is true, then we print the value of x
# #     print(x)
# #     # with x = x + 1, we increment x by 1
# #     x = x + 1
# #     # the condition is tested again...until the condition is false. When x is greater than 5, the loop stops.

# # for county in counties:
# #     print(county)

# numbers = [0, 1, 2, 3, 4]
# # for num in numbers:
# #     print(num)

# # for num in range(5):
# #     print(num)

# # indexing can also be be used to iterate through a list.
# # the variable i is used to indicate the index, or the values 0, 1, 2, in the lenth of the counties list. any variable can be used.
# # inside the range function, we get the length of the list of counties, which is the integer 3.
# # then, we iterate throught the list, where the variable i is equal to 0 for the first index. 
# for i in range(len(counties)):
#     print(counties[i])





#using f strings
# my_votes = int(input("How many votes did you getin the election?"))
# total_votes = int(input("What is the total votes in the election?"))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# #using f strings and dictionaries
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

voting_data = [' '{"county":"Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters:: 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, registered_voters in voting_data:
    print(f'{'county'} county has {'registered_voters'} registered voters.')





