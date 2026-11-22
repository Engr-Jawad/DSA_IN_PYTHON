from array import *
def reverse_arr(arr):
    n = len(arr)
    for i in range(n//2):
        j = n-1-i
        arr[i],arr[j] = arr[j],arr[i]
        
    print(arr)



if __name__ == "__main__":
    arr = array("i",[10, 20, 30, 40, 50])
    print(reverse_arr(arr))
