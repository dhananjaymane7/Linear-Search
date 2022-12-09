def linear_search(list,key):
    for i in range(0,len(list)):
        if(list[i]==key):
            return i
    return -1
list=[]
n=int(input("Enter how many elekemts do you want to add in list :"))
for i in range(n):
    n1=int(input("Enter elements :"))
    list.append(n1)
key=int(input("Enter element do you want to search:"))
res=linear_search(list,key)
if res==-1:
    print("Element not found")
else:
     print("Element found at :",res)
