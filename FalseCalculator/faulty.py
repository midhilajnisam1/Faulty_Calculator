#Hey guys this is my first python exercise which i named it as Faulty Calculator if you enter the below numbers it will show the false o/p
#56 + 25 = 567
#30 - 15 = 4
#260 * 6 = 1880
#880 / 45 = 123



#Gives the choices for users

print("""
1 for Addition
2 for Subtraction
3 for Multiplication
4 for Division
""")

#Gets the details from the user

choice = input("Enter one of the operation from above to perform: ")
v1 = int(input("Enter a number: "))
v2 = int(input("Enter a second number: "))


#If user enter 1

if choice == "1" :
    if v1 == 56 and v2 == 25:
        print("Answer is 567")
    else:
        print("Anwer is",v1+v2)
#If user enters 2

elif choice == "2":
    if v1 == 30 and v2 == 15:
        print("Answer is 4")
    else:
     print("Answer is", v1-v2)
#If user enters 3

elif choice == "3":
    if v1 == 260 and v2 == 6:
        print("Anwer is 1880")
    else:
     print("Answer is", v1*v2)
#If user enters 4

elif choice == "4":
    if v1 == 880 and v2 == 45:
        print("Answer is 123")
    else:
     print("Answer is ", v1/v2)
#This will show if the user inputs any other element which is not given in choice

else:
 print("Invalid Input")








