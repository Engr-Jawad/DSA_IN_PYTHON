import array
def insertion_sort(arr):
    for i in range(n):
        current = arr[i]
        previous = i-1
        while(previous >= 0 and arr[previous] > current):
            arr[previous+1] = arr[previous]
            previous = previous -1 

        arr[previous+1] = current


    return arr


if __name__ == "__main__":
    n = int(input("enter the size of the arry : "))
    arr = array.array("i",[])
    for i in range(n):
        user_input = int(input("Enter element in the array : "))
        arr.append(user_input)

    print("insertion sort : ",insertion_sort(arr))
    