import array 
def sum_of_array(arr):
    sum = 0
    n = len(arr)
    for i in range(n):
        sum += arr[i]
    return f"sum of the array : {sum}"



if __name__ == "__main__":
    arr = array.array("i",[10,10,20,30,40,50])
    print(sum_of_array(arr))