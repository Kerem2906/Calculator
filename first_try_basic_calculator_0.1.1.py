Number1 = float(input("Please enter first number :"))
Number2 = float(input("Please enter second number :"))

Operation = input("Please show the operation type you want with '+' , '-' , '*' or '/' symbols :")

if Operation in ('x' , 'X' , '*'):
   Result = Number1 * Number2
elif Operation == '+':
   Result = Number1 + Number2
elif Operation == '-':
   Result = Number1 - Number2
elif Operation == '/':
   Result = Number1 / Number2
else:
   Result = None #Realized if wrong or an Operation I didn't add is entered it gives an error so a quick fix
   print("Please enter a valid operation!")

if Result is not None:
   print(Number1, Operation, Number2, "=", Result) #I removed float because it was both unnecessary and letting an error happen