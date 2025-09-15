# Normally I thought another code would do the work (like continue loops)
# Yet it turned out 'while True' command is better (in my opinion)
# So I did my best to use 'while True' successfully
while True:

    while True:
        try:
            Number1 = float(input("Please enter first number :"))
            break
        except ValueError:
            print("Please enter a valid number !")

    while True:
        try:
            Number2 = float(input("Please enter second number :"))
            break
        except ValueError:
            print("Please enter a valid number !")

    while True:
            Operation = input("Please show the operation type you want with '+' , '-' , '*' or '/' symbols :")
            if Operation in ('x', 'X', '*', '+', '-','/'):  # This didn't come to my mind at first ,so I take a hint from AI :/
                break                                       # Well , before I tried couple ways , it didn't work around sadly
            print("Please enter a valid operation!")
        # 'try' and 'except' values are removed because they are unnecessary and gives errors

    if Operation in ('x', 'X', '*'):
       Result = Number1 * Number2
    elif Operation == '+':
       Result = Number1 + Number2
    elif Operation == '-':
       Result = Number1 - Number2
    elif Operation == '/':
       Result = Number1 / Number2

    print("Here is your result : ",Number1 ,Operation ,Number2, '=', Result)


