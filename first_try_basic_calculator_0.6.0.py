history = []


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
        if Operation in ('x', 'X', '*', '+', '-', '/'):
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

    print("Here is your result : ", Number1, Operation, Number2, '=', Result)
    for h in history:
        print("Here is your previous output : ", h[0], h[1], h[2],'=', h[3])
    while True:
        ask = input("Do you want to continue ? (Y/N):")
        if ask.lower() in ('y', 'yes'):
            history.append((Number1, Operation, Number2, Result))
            break
        elif ask.lower() in ('n', 'no'):
            quit()
        else:
            print("Please make a valid decision")
            continue





