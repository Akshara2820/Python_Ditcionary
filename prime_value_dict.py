dic={1:2,2:3,3:4,4:1,5:8}
for i in dic:
    x=dic[i]
    if x>1:
        j=2
        while j<x:
            if x%j==0:
                print("not prime no,",x)
                break
            j+=1
        else:
            print("prime no--",x)
    else:
        print("it is small than 1--",x)







# a=2
# while a<=100:
#     b=2
#     while b<a:
#         if a%b==0:
#             break
#         b+=1
#     else:
#         print(a)
#     a+=1
