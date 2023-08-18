# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi_score = weight/(height ** 2)

if bmi_score < 18.5:
    print("Your BMI is " + str(round(bmi_score)) + ", you are underweight.")
elif bmi_score < 25:
    print("Your BMI is " + str(round(bmi_score)) + ", you have a normal weight.")
elif bmi_score < 30:
    print("Your BMI is " + str(round(bmi_score)) + ", you are slightly overweight.")
elif bmi_score < 35:
    print("Your BMI is " + str(round(bmi_score)) + ", you are obese.")
else:
    print("Your BMI is " + str(round(bmi_score)) + ", you are clinically obese.")