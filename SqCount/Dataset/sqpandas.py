import pandas

sqdata = pandas.read_csv("Squirrel_Data.csv")

-- way1

sqdata_color = sqdata["Primary Fur Color"]

countGray = 0
countCin = 0
countBl = 0
countNan = 0

for color in sqdata_color:
    if color == "Black":
        countBl += 1
    elif color ==  "Gray":
        countGray += 1
    elif color == "Cinnamon":
        countCin += 1
    else:
        countNan += 1

print(countBl)
print(countGray)
print(countCin)
print(countNan)


sq_count = {
    "color": ["Black", "Gray", "Cinnamon"],
    "count": [countBl, countGray, countCin]

}

pandas.DataFrame(sq_count).to_csv("SqcountColor.csv")


--way2

gray_sqcount = len(sqdata[sqdata["Primary Fur Color"] == "Gray"])
black_sqcount = len(sqdata[sqdata["Primary Fur Color"] == "Black"])
cin_sqcount = len(sqdata[sqdata["Primary Fur Color"] == "Cinnamon"])


data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [gray_sqcount, black_sqcount, cin_sqcount]
}

pandas.DataFrame(data_dict).to_csv("SqcountColorr.csv")
