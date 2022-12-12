def sentinel_search(arr,length,key):
    last=arr[length-1]
    arr[length-1]=key
    i=0

    while(arr[i]!=key):
        i+=1
    arr[length-1]=last
    if((i<length-1) or (arr[length-1] == key)):
        print(key, "is present at index", i)
    else:
        print("Element Not found")
arr=[]
length=len(arr)
n=int(input("Enter elements do you want to add in array :"))
for i in range(n):
    n1=int(input("Enter elements in the array :"))
    arr.append(n1)
key=int(input("Enter element to be search :"))
sentinel_search(arr, length, key)
