alpha=["a","b","c","d","e"]
d={}
i=0
l=len(alpha)
while i<l:
    d[alpha[i]]=i+1
    i+=1
print(d)





# 2nd question
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }
dic={}
d=sampleDict["name"]
d1=sampleDict["salary"]
d2=sampleDict["age"]
dic["name"]=d
dic["salary"]=d1
dic["age"]=d2
print(dic)



# nested dictionary creat
dic={}
i=1
while i<=3:
  dic[i]={}
  n=int(input("enter key--"))
  n1=input("enter value--")
  dic[i]={n:n1}
  i+=1
print(dic)
  