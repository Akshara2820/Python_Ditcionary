dic={1:1,2:2,3:3,4:4}
def check(key):
    if key in dic:
        print("key is define")
    else:
        print("key is not define")
n=int(input("enter no--"))
check(n)