
emplArr = [[0]*5 for i in range(5)]
sorter_check = False
exit_case = False

def fnameAdd(i,j,firstName):
    emplArr[i][j] = firstName

def lnameAdd(i,j,lastName):
    emplArr[i][j] = lastName

def nationAdd(i,j,nationality):
    emplArr[i][j] = nationality

def salaryAdd(i,j,amount):
    emplArr[i][j] = amount

def emailAdd(i,j,mail):
    emplArr[i][j] = mail


def table_arr(arr):
    
    headers = ["First Name","Last Name","E-Mail","Salary","Nationality"]
    column_widths = [len(header) for header in headers]  
    
  
    for row in arr:
        for i, column in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(column)))
    
    
    for i, header in enumerate(headers):
        print(header.ljust(column_widths[i] + 2), end="")
    print()
    
    
    for row in arr:
        for i, column in enumerate(row):
            print(str(column).ljust(column_widths[i] + 2), end="")
        print()

def addEmp():
    fnameAdd(0,0,"Dave")
    lnameAdd(0,1,"Mathew")
    emailAdd(0,2,"dave12mathew@gmail.com")
    salaryAdd(0,3,10000)
    nationAdd(0,4,"British")

    fnameAdd(1,0,"Bharath")
    lnameAdd(1,1,"Dev")
    emailAdd(1,2,"b.dev22@gmail.com")
    salaryAdd(1,3,100000)
    nationAdd(1,4,"Indian")

    fnameAdd(2,0,"Lee")
    lnameAdd(2,1,"Kim")
    emailAdd(2,2,"l.kim99@gmail.com")
    salaryAdd(2,3,14000)
    nationAdd(2,4,"Korean")

    fnameAdd(3,0,"John")
    lnameAdd(3,1,"Haruhi")
    emailAdd(3,2,"harujohn@gmail.com")
    salaryAdd(3,3,20000)
    nationAdd(3,4,"Japanese")

    fnameAdd(4,0,"George")
    lnameAdd(4,1,"Cooper")
    emailAdd(4,2,"cooper.g24@gmail.com")
    salaryAdd(4,3,30000)
    nationAdd(4,4,"American")
addEmp()


#def sort_by_fname(arr,index):
def sorter(arr,index):
    arr.sort(key = lambda x : x[index-1])
    table_arr(arr)
def rev_sorter(arr,index):
    arr.sort(reverse = True,key = lambda x : x[index-1])
    table_arr(arr)


def fin_sorter(arr):
    
    table_arr(emplArr)
    print("\nHow do you want your list to be sorted\n")
    print("Please select one of the following \nFirst Name == 1 \nLast Name == 2 \nE-mail == 3 \nSalary == 4 \nNationality == 5")
    user_input = int(input("\nEnter Here: "))

    match user_input:
            case 1: 
                print("\nSorting by First Name\n")
                ascinp = input("Ascending or Descending \n Please select A or D: ")
                if ascinp == "A":
                    sorter(arr,user_input)
                else:
                    rev_sorter(arr,user_input)
            case 2: 
                print("\nSorting by Last Name\n")
                ascinp = input("Ascending or Descending \n Please select A or D: ")
                if ascinp == "A":
                    sorter(arr,user_input)
                else:
                    rev_sorter(arr,user_input)
                
            case 3: 
                print("\nSorting by E-mail\n")
                ascinp = input("Ascending or Descending \n Please select A or D: ")
                if ascinp == "A":
                    sorter(arr,user_input)
                else:
                    rev_sorter(arr,user_input)
            case 4: 
                print("\nSorting by Salary\n")
                ascinp = input("Ascending or Descending \n Please select A or D: ")
                if ascinp == "A":
                    sorter(arr,user_input)
                else:
                    rev_sorter(arr,user_input)
            case 5: 
                print("\nSorting by Nationality\n")
                ascinp = input("Ascending or Descending \n Please select A or D: ")
                if ascinp == "A":
                    sorter(arr,user_input)
                else:
                    rev_sorter(arr,user_input)
            case _:
                raise Exception()
                
x_var = ""
while x_var == "":
   
    while sorter_check == False:
        try:
            print("-----------------------------------------------------------------------------\n")
            fin_sorter(emplArr)
        except ValueError:
            print("Enter a number as shown below\n Please try again")
        except Exception:
            print("Please try Again")
        else:
            inp = input("")
            if(inp == "X"):
                x_var = " "
                sorter_check = True