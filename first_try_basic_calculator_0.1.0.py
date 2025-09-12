#Changed base variables to English so perhaps because that will matter in the future idk


Number1 = float(input("Please enter first number :"))
Number2 = float(input("Please enter second number :"))

Operation = input("Please show the operation type you want with '+' , '-' , '*' or '/' symbols :")

if Operation in ('x' , 'X' , '*'): #I realized in command would make lot more sense
   Result = Number1 * Number2
elif Operation == '+':
   Result = Number1 + Number2
elif Operation == '-':
   Result = Number1 - Number2
elif Operation == '/':
   Result = Number1 / Number2
else: #Also using elif was more work and seems more complicated in a situation like that so i used else (just forgot the else command :D)
   print("Please enter a valid operation!")

print(Number1, Operation, Number2, "=", float(Result)) #Added this command so people can see the whole problem in one piece