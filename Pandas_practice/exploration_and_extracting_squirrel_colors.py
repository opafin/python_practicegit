# import csv
import pandas

# with open("weather_data.csv") as file:
# weather_data = csv.reader(file)
# temperatures = []
#     for index, row in enumerate(weather_data):
#         # print(row)
#         if index == 0:
#             temperatures.append(row)
#         else:
#             temperatures.append([row[0], int(row[1]), row[2]])
# for line in temperatures:
#     print(line)
#     print(type(line[1]))


# data = pandas.read_csv("weather_data.csv")

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])

# data_dictionary = data.to_dict()
# print(data_dictionary)

# print(data[data.day == "Monday"])
# monday = data[data.day == "Monday"]


# def fahreinheit_conversion(x):
#     x = x * 1.8 + 32
#     return x


# print(f"Mondays temperature in fahrenheit: {fahreinheit_conversion(int(monday.temp.item()))}")

# data_dict = {
#     "students": ["Geralt", "Ciri", "Eskiel"],
#     "scores": [80, 90, 70]
# }
# print(data_dict)
# student_data = pandas.DataFrame(data_dict)
# print(student_data)

squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
trimmed_data = squirrel_data["Primary Fur Color"]
cinnamons = trimmed_data[trimmed_data == "Cinnamon"]
blacks = trimmed_data[trimmed_data == "Black"]
grays = trimmed_data[trimmed_data == "Gray"]

squirrels_by_color = {
    "Primary Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [len(blacks), len(grays), len(cinnamons)]
}

panda_squirrels_by_color = pandas.DataFrame(squirrels_by_color)
print(panda_squirrels_by_color)

panda_squirrels_by_color.to_csv('squirrel_colors.csv')
