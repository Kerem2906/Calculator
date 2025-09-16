#Added 'Do you want to continue ?' question for practice , i probably remove this feature after i make a GUI
#But for now , practice is a practice i guess :)
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
            if Operation in ('x', 'X', '*', '+', '-','/'):
                break
            print("Please enter a valid operation!")


    if Operation in ('x', 'X', '*'):
       Result = Number1 * Number2
    elif Operation == '+':
       Result = Number1 + Number2
    elif Operation == '-':
       Result = Number1 - Number2
    elif Operation == '/':
       Result = Number1 / Number2

    print("Here is your result : ",Number1 ,Operation ,Number2, '=', Result)

    while True:
        ask = input("Do you want to continue ? (Y/N):")
        if ask.lower() in ('y', 'yes'):
            break
        elif ask.lower() in ('n', 'no'):
            quit()
        else:
            print("Please make a valid decision")
            continue



