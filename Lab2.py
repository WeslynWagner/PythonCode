"Weslyn Wagner(zfs119): lab2.py, for Python3"

f = open("c:\\Users\\cvall\\Desktop\\CloudComputing\\c.txt","r")


origlist = f.readlines()
dataDict ={}

total = 0
for line in origlist:
    row = line.split()
    date = row[0]
    value = row[2]
    if date not in dataDict:
        dataDict[date]=value
        total = 0

    total = total + int(value)
    if date in dataDict:
        dataDict[date] = total

f.close()
"""
def maxValue(dict):
    value = 0
    for key in dict:
        if dict[key]> value:
            value = dict[key]
            date = key
    return print("The max value is %s and occurs on %s" %(value,date))

def minValue(dict):
    value = 9999999999
    for key in dict:
        if dict[key]< value:
            value = dict[key]
            date = key
    return print("The min value is %s and occurs on %s" %(value,date))
"""    

maxValue= max(dataDict.values())
minValue= min(dataDict.values())
print("The max value is %s" %(maxValue))
print("The min value is %s" %(minValue))



sortedDict = sorted(dataDict.items())
for i in sortedDict:
    print("%s: %s" %(i[0],i[1]))
