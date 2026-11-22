from array import *
def liner_Search(arr):
    target = int(input("enter the target value : "))
    for i in range(len(arr)):
        if arr[i] == target:
            return f"target exisit : {target}"
            break
    else:
        return f"target not exisit"






if __name__ == "__main__":
    arr = array("i",[5, 10, 15, 20, 25, 30])
    print(liner_Search(arr))
    