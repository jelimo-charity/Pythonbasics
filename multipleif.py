print("Welcome to the Rollercoaster!")

height=int(input("What is your height?\n"))
bill=0
if height >=120:
    print("You can ride the rollercoaster")
    age=int(input("Enter your age: \n"))
    
    if age<12:
        bill+= 7
        print("pay $7")
    elif age<18:
        bill+= 8
        print("pay$8")
    elif age<25:
        bill+= 10
        print("pay $10")
    else:
        bill+= 12
        print("pay $12")
        want_photo=input("Do you want a photo? Yes or No\n")
    if want_photo=="Yes":
        bill==bill+4
        print(f"Your final bill is ${bill}")
        
else:
    print("You need to grow in height to ride the coaster")