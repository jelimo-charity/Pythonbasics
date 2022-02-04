print("Let us calculate the love score!")
her_name=input("Enter her name:\n")
his_name=input("Enter his name:\n")
love_name=her_name+his_name

lower_case=love_name.lower()
t=love_name.count("t")
r=love_name.count("r")
u=love_name.count("u")
e=love_name.count("e")
true=t + r + u + e

l=love_name.count("l")
o=love_name.count("o")
v=love_name.count("v")
e=love_name.count("e")

love= l + o + v + e


love_score= (true) + (love)
if (love_score <5) or (love_score >7):
    print(f"Your love score is {love_score}, You go together like coke and mentos")
elif (love_score>=5) and (love_score<=7):
    print(f"Your score is{love_score}, You go alright together")
else:
    print(f"Your love score is {love_score}")


