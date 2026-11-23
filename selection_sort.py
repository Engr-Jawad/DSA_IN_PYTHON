
import array 
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest = arr[i]
        for j in range(i+1,n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i],arr[smallest] = arr[smallest],arr[i]
    return arr


if __name__ == "__main__":
    arr = array.array("i",[4,1,2,3,5])
    print(selection_sort(arr))