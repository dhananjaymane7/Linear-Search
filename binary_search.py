def binary_search(arr,low,high,key):
    if high>low:
        mid=(high+low)//2
        if(arr[mid]==key):
            return mid
        elif (arr[mid]>key):
            return binary_search(arr,low,mid-1,key)
        else:
            return binary_search(arr,mid+1,high,key)
    else:
        return -1
arr=[]
n=int(input("How many elements do you want to add in array :"))
for i in range(n):
    n1=int(input("Enter elements in the array :"))
    arr.append(n1)
key=int(input("Enter element to be search"))
result=binary_search(arr,0,len(arr)-1,key)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

