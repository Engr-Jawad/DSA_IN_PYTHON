import array

def partition(arr,st,end):
    idx = st -1
    pivot = arr[end]
    for j in range(st,end):
        if arr[j] < pivot:
            idx+=1
            arr[j],arr[idx] = arr[idx],arr[j]
    idx+=1
    arr[end],arr[idx] = arr[idx],arr[end]
    return idx
        


def quick_sort(arr,st,end):
    if st < end:
        pivotidx = partition(arr,st,end)
        quick_sort(arr,st,pivotidx-1)
        quick_sort(arr,pivotidx+1,end)
    return arr

    


if __name__ == "__main__":
    arr = array.array("i",[5,2,6,4,1,3])
    print(quick_sort(arr,0,len(arr)-1))