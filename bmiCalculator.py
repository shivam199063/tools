# This is BMI calculator made by shivam saini. gmail: shivam199063@gmail.com
name=input("Please enter your good name : ")
# declare age:
age=int(input(f"Hello,{name} Please enter your age :"))
# declare weight:
print(f"\n{name.upper()},\n     IF you know your weight in \"POUND\" than press :1\n       if you know your weight in \"KG\" than press :2 ")
weightType=int(input(":"))
if weightType ==1:
    weight=float(input(f"Enter your weight in Pound : "))
    weight*=.454
elif weightType ==2:
    weight=float(input(f"Enter your weight in KILOGRAM : "))
else:
    print("choose a right option ,Please try again")
    # declare height:
print(f"\n\n{name.upper()},\n    IF you know your height in \"METRE\" than press :1\n    if you know your height in \"FOOT\" than press :2 ")
heightType=int(input(":"))
if heightType == 1:
    height=float(input(f"Enter your height in Metre : "))
elif heightType == 2:
    height=float(input(f"Enter your height in Foot : "))
    height*=.30
else:
    print("choose a right option ,Please try again")

# calculate BMI:
bmi=weight/height**2
if 18.5 < bmi <25:
    print(f"\nHii {name},\n \n       your BMI is {bmi} .so you maybe happy \U0001F604 because your BMI is in HEALTHY range.")
elif 25<bmi<=40:
    print(f"\nHii {name},\n \n       your BMI is {bmi} .so this is not good for your health \U0001F620 because your BMI is in OVERWEIGHT range. \n so you can decrease your daily Deight, please")
elif bmi<18:
    print(f"\nHii {name},\n\n        your BMI is {bmi} .so this is not good for your health \U0001F620 because your BMI is in UNDERWEIGHT range.\n  so you can take healthy Deight, please.")
elif bmi>=40:
    print(f"\nHii {name},\n\n        your BMI is {bmi} .so this is not good for your health \U0001F620 because your BMI is MORBIDLY OBESE range.\n  so you can DECREASE your daily Deight, please.")
else:
    print("wrong entry")



print("\n                  \"I WISH FOR YOUR HEALTHY LIFE\"  ")