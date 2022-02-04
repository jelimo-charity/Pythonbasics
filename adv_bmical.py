weight=input("Enter your weight in kg: \n") 
height=input("Enter your height in m: \n")
new_weight=int(weight)
new_height=float(height)
BMI=new_weight/(new_height)**2
New_BMI=int(BMI)
if New_BMI<18.5:
    print("You're Underweight.")
elif New_BMI<25:
    print("You have Normal weight.")
elif New_BMI<30:
    print("You're Overweight.")
elif New_BMI<35:
    print("You're Obese.")
else:
    print("You're clinically obese.")
