#Realized putting anything other than a number for first two commands gives an error so after some search I figured it out and make a new error message.
Repeat = [1]
Loop = 0
while Loop < len(Repeat): #Sadly figuring this out take more time than I expected ,but I figured it out ,and finally I have an endless loop.
    try:
        Number1 = float(input("Please enter first number :"))
    except ValueError:
        print("Please enter a valid number !")
        exit()
    try:
        Number2 = float(input("Please enter second number :"))
    except ValueError:
        print("Please enter a valid number !")
        exit()

    Operation = input("Please show the operation type you want with '+' , '-' , '*' or '/' symbols :")

    if Operation in ('x', 'X', '*'):
        Result = Number1 * Number2
    elif Operation == '+':
        Result = Number1 + Number2
    elif Operation == '-':
        Result = Number1 - Number2
    elif Operation == '/':
        Result = Number1 / Number2
    else:
        Result = None
        print("Please enter a valid operation!")

    if Result is not None:
        print("Here is your result :", Number1, Operation, Number2, "=",
              Result)

#I will figure something out for quit command , try to make a loop for every value so if there is something wrong instead of stopping it will continue in a loop.





