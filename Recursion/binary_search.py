import random as rnd

int_list = list()

for num in range(int(input("Enter the range for the List"))):
    int_list.append(rnd.randint(1,100))
    
print(int_list)

int_list.sort()
print(int_list)

def binary(data,target,low,high):
    
    if low > high:
        return False
    else:
        mid = int((low + high) / 2)
        print("Mid-point is:",mid)
        print("Low-point is:",low)
        print("High-point is:",high)
        print("------------------------------------------------------------")
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary(data,target,low,mid-1)
        else:
            return binary(data,target,mid+1,high)

result = binary(int_list,int(input("Enter the number to find")),0,len(int_list)-1)

print(result)