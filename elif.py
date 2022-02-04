print("Welcome to the Rollercoaster!")
height=int(input("What is your height?\n"))
if height >=120:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age: \n"))
    if age<12:
        print("pay $7")
    elif age<18:
        print("pay$8")
    elif age<25:
        print("pay $10")
    else:
        print("pay $12")
else:
    print("You need to grow in height to ride the coaster")