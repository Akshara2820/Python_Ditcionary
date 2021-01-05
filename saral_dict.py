# update dict 
# op-{1: 10, 2: 40, 3: 30, 5: 50, 6: 60}
'''
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
'''
# find key
'''
dict1={"name":"Akshara","age":18}
if "name" in dict1:
    print("yes")
else:
    print("no")
'''

# print sum all values
'''
my_dict = {
        'data1':100,
        'data2': -54,
        'data3': 247
} 
print(sum(my_dict.values()))
'''

# without using sum function
'''
my_dict = {
        'data1':100,
        'data2': -54,
        'data3': 247
} 
b=0
for i in(my_dict):
    b=b+ my_dict[i]
print(b)
'''

'''
dict =	{ 5:{
                1: 'NAVGURUKUL',
                2: 'IN'},  
  	    3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
        
dict.pop(5)

print(dict)
'''

# append in dictionary
'''
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
s=[]
d={}
i=0
l=len(list1)
while i<l:
    d[list1[i]]=list2[i]
    i+=1
print(d)
'''

# duplicate keys ko remove karna hai
'''
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }
print(dic)
'''

# user se input se lekar dictionary append karvana hai
'''
n=int(input("enter no--"))
d={}
for i in range (n):
    name=input("enter name--")
    marks=int(input("enter no--"))
    d[name]=marks
print(d)
'''


# dict1={"akshara":["radha","arti","subham"],"mishra"["sharma","kushvah",]}
# c=0
# i=0
# l=len(dict1)
# while 


# l=[12,13,14,15]
# # for i in l:
# #     print(i,"a")
# #     print(l[i])
# i=0
# while i<l:
#     print(i,"ak")
#     print(l[i])
#     i+=1



# n=[12,13,14,15]
# i=0
# while i<len(n):
#     print(n[i])
#     i+=1
# dic={0:1,2:2,3:3}
# for i in dic:
#     print(dic[i])
#     for j in dic:
#         print(dic[j])

# dic={1:3,3:2,2:4,5:1}
# s=[]
# max=dic
# for i in dic:
#     print(dic[i])
#     if dic[i]>max:
#         if dic[i] not in s:
#             s.append(dic[i])
# print(s)

# alpha_value=dict.fromkeys(str.ascii_lowercase,range(0))
# i=1
# for k,v in alpha_value.iteritems():
#     alpha_value[k]=[i]
#     i+=1
# print(alpha_value)
