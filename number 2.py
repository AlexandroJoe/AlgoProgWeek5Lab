def userinput():
    a = eval(input("Enter the height: "))
    for i in range(a):
        print(" "*(a-i), "*"*(i*2+1))
    for i in range(a-2, -1, -1):
        print(" "*(a-i), "*"*(i*2+1))
#SorryCannot1Loop
userinput()