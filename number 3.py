import math
def userinput(number):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                print("False !")
                break
        else:
            return number
    else:
        print("False !")
Result = 0
def Result_Int(Num):
    global Result
    if(Num > 0):
        Reminder = Num %10
        Result = (Result *10) + Reminder
        Result_Int(Num //10)
    return Result
def emirpCheck(number):
    d = userinput(number)
    e = Result_Int(number)
    if  d == e:
        print("False !")
    else:
        print(d,e)
emirpCheck(5)
