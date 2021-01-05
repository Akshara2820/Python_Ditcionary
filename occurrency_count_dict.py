name="MISSISSIPPI"
name1=list(name)
index=0
length=len(name1)
list1=[]
while index<length:
    j=0
    count=0
    while j<length:
        if name1[j]==name1[index]:
            count+=1
        j+=1
    if [name1[index]] not in list1:
        list1.append([name1[index],count])
    index+=1
print(dict(list1))