import random


rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))

arr = []
 
def arr_printer(arr):
    for i in range(rows):
        for j in range(columns):
            print(arr[i][j], end=" ")
        print()
        
        

value = int(input("Please enter a range"))

arr = [[random.randint(0,value)for i in range(columns)]for j in range(rows)]
print(arr)
print("Do you want to sort your array in ascending or descending format")
prompt = input("Please input A or D")
if prompt == "A":
    for i in range(len(arr)):
        #first loop goes through the rows
        for j in range(len(arr[i])):
            #second loop goes through the columns
            for k in range(len(arr[i]) - 1):
                #third is used to go through check values row wise  
                if arr[i][k] > arr[i][k+1]:
                    temp = arr[i][k]
                    arr[i][k] =  arr[i][k+1]
                    arr[i][k+1] = temp
                
    print(arr)
    arr_printer(arr)
else :
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i]) - 1 ):
                if arr[i][k] < arr[i][k+1]:
                    temp = arr[i][k] 
                    arr[i][k] = arr[i][k+1]
                    arr[i][k+1] = temp
    print(arr)
    arr_printer(arr)
    
    
