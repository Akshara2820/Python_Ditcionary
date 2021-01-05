my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
s=[]
for i in my_dict.values():
    s.append(i)
s=[50, 58, 56, 40, 100, 20]
i=0
l=len(s)
a1=[]
c=0
while i<l:
    j=0
    while j<l:
        if s[j]>s[i]:
            if s[j] not in a1:
                a1.append(s[j])
        j+=1
    break
    i+=1
print(a1)




# find keys
my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
from heapq import nlargest
max1= nlargest(3,my_dict,key=my_dict.get)
print(max1)


# without function
my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
s=[]
s1=[]
for i in my_dict.values():
    s.append(i)
for j in my_dict.keys():
    s1.append(j)
var1=0
var2=0
n=0
l=len(s)
s2=[]
while n<l:
    n1=0
    while n1<l:
        if s[n1]>s[n]:
            if s1[n1] not in s2:
                s2.append(s1[n1])
        n1+=1
    break
    n+=1
print(s2)
            