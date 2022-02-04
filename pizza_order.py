print("Welcome to Pizza Deliveries!")
pay=0
size=input("What size of pizza do you want? S/M/L \n")
add_pepperoni=input("Do you want pepperoni? yes/no\n")
if size=="S":
    pay+=15
    if add_pepperoni=="yes":
        pay+=5
    print(f"Small pizza: ${pay}")
elif size=="M":
    pay+=20
    if add_pepperoni=="yes":
        pay+=10
    print(f"Medium pizza: ${pay}")
else:
    pay+=25
    if add_pepperoni=="yes":
        pay+=15
    print(f"Large pizza: $ {pay}")
   
    
    

