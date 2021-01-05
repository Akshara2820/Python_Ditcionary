sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

v=sampleDict["city"]
del sampleDict["city"]
sampleDict["location"]=v
print(sampleDict)

# sampleDict["location"] = sampleDict.pop("city")
# print(sampleDict)