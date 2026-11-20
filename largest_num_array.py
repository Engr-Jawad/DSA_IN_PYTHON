import array
arr = array.array("i",[5,6,90,40,30,20,100,88,78,-39,-56])
def largest_num(arr):
    largest = 0 
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return f"Largest number in the array : {largest}"

print(largest_num(arr))
