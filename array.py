import array
num = array.array("i",[1,2,3,4,5,6,7,8])
print("array : ",num)


# loop on the array 
for i in range(len(num)):
       print(i,end=" ")


print("\n")

# enhanced loop 
print("Enhanced loop")
for i in num :
       print(i,end=",")





# insertion in array 
# array_name.insert(index,value)
num.insert(0,200) 
print("\nafter insertion array : ",num) # it will change the original array 



# append element in array 
# array_name . append(value)
num.append(50)
print("\nafter element append in the array : ",num) # it add the element in the last of the array .


# pop function 
# array_name.pop(index_value) if we not pass the index value it will delete the last element in the array .
num.pop()
print("after poping the last element deleted : ",num)

# typecode of the array 
# typecode mean data type of the array 
print("Data type of the array : ",num.typecode)


# remove element from the array 
# arrray_name . remove(value) it will remove that value from the array but its first occurence .
num.remove(4)
print(num)

# slicing 
marks = array.array("i",[66,77,88,99,89,76,65,54])
print(marks[0:3]) # it will print 66,77,88 
print(marks[::-1]) # reverse the array 


# taking input from the user 
roll_num = array.array("i",[])
n = int(input("enter the size of the array : "))
for i in range(n):
       user_input = int(input("enter element in the array : "))
       roll_num.append(user_input)

for j in roll_num:
       print(j,end=" ")



