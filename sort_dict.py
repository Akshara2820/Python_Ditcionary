name={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
s=sorted(name.values())
dict1={}
for i in s:
    for j in name.keys():
        if name[j] == i:
            dict1[j] = name[j]
            break
print(dict1)


