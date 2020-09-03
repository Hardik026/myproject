'''s=6
if (s==6):
    print("yes")'''
e=-1
arr=list()
for x in range(0,5):
    #ele=int(input())
    arr.append(int(input()))
s=int(input("enter the element to be searched"))
for x in range(0,5):
 if (arr[x] == s):
     e=5
     print( s,"is found at ",x)
if(e==-1):
    print("not found")
