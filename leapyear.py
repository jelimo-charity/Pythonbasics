#checking if a year is a leap year
year=int(input("Enter the year you would like to check: \n"))
if year%4:
    print("Leap Year.")
elif year% 100:
    print("Not a Leap Year")
elif year%400:
    print("Leap Year.")
else:
    print("Not Leap year")