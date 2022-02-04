import random
names= input("Enter the names of the people in the party\n")
dnames=names.split(", ") 
no_names=len(dnames)
random_choice=random.randint(0,no_names-1)
person_to_pay= dnames[random_choice]
print(person_to_pay +" "+ "is going to pay the bill")