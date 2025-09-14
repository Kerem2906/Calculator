#This is working right now but it looks really terrible at the moment , I will learn something better for it but at the moment this will be base 0.3.0 update.

Repeat = [1]
Loop = 0
while Loop < len(Repeat):
    while True: #I used 'while True' commands to make a loop until a right input is given , but it makes it really long.
        try:
            Number1 = float(input("Please enter first number :"))
        except ValueError:
            print("Please enter a valid number !")
            break

        while True:
            try:
                Number2 = float(input("Please enter second number :"))
            except ValueError:
                print("Please enter a valid number !")
                break #It takes a lot of time for me to understand why break commands not work as i wanted while in a loop in a loop in a loop
                      #Still if i enter a wrong value for second one it starts from first input , i guess because there is a loop in a loop , at least that's the only outcome in my mind.
            while True:
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
                    break

                if Result is not None:
                    print("Here is your result :", Number1, Operation, Number2, "=",
                          Result)
                break
            break #In the end i finished this but i guess i will need a better version so i will look for other commands to see more suitable alternative , it may be 0.4.0 or 0.3.5 i dont know for sure.










