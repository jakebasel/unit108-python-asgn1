"""
script: simple calc
Author: jake basel
year: 2021
functionality: basic math
"""

# imports


# globals


# functions

def print_menu():
    print("-" *30)
    print(" pycalc")
    print("-"*30)

    print("[1]-sum")
    print("[2]-subtract")
    print("[3]-multiply")
    print("[4]-division")
    print("[5]-is it even")
    print("[q]-Quit")


# instructions
selected_option=""
while(selected_option != "q"):

    print_menu()
    selected_option = input("please select an option: ")

    if(selected_option=="q"):
        break
    
    num1 = float(input("choose first number: "))
    if(selected_option=="5"):
        print("")
    else:
        num2 = float(input("choose second number: "))

    if(selected_option=="1"):
        result = num1 + num2
        print(result)
    elif(selected_option=="2"):
        result = num1 - num2
        print(result)
    elif(selected_option=="3"):
        result = num1*num2
        print(result)
    elif(selected_option=="4"):
        if(num2==0):
           print("error can not divide by 0")
        else:
            print(num1/num2)   
    elif(selected_option=="5"):     
        if(num1 % 2 == 0):
            print("number is even")
        else:
            print("number is not even")

    
print("good bye")

    

