# Project:      Lab 2 (AnhTrinhLab02Sec03.py)
# Name:         Anh Trinh
# Date:         01/11/16
# Description:  A program will print out numbers 0-9
#               then modify to print out numbers 1-10
#                                        numbers 0-9 1st Column
#                                                10-19 2nd Column

def main():

    #Greeing
    print("Welcome To The Program!"
          "\n------------------------\n")


    print("Printing out numbers 0-9...")
    for i in range(10):
        print(i)

    print()
    
    
    #i starts at 0 -> +1 helps turning 0 -> 1 and go on 9 -> 109
    print("Printing out numbers 1-10...")
    for i in range(10):
        print(i+1)
         
    print()
    

    print("Printing 0-9 in the 1st column & 10-19 in the 2nd column...")
    print("1st column           2nd column")
    for i in range(10):
        print("  ",i,"                  ",i+10)
    
main()
