import array
def smallest_num(arr):
    smallest = 0
    n = len(arr)
    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]
    return f"Smallest number in the array : {smallest}"


if __name__ == "__main__":
    arr = array.array("i",[50,30,20,10,100,98,89,-3,-30,-20,20,12])
    print(smallest_num(arr))