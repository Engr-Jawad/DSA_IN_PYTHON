import array
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__ == "__main__":
    n = int(input("enter the size of the array : "))
    arr = array.array("i",[])
    for i in range(n):
        user_input = int(input("enter element in the array : "))
        arr.append(user_input)
    
    print("Sorted array : ",bubble_sort(arr))