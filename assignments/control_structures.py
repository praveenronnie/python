# Print statement
print("Welcome to Assignment-1")
print("\n")

# Addition of 2 numbers
Num1 = 10
Num2 = 30
Add = Num1 + Num2
print("Num1= ", Num1)
print("Num2= ", Num2)
print("Add= ", Add)
print("\n")

# Calculating BMI

bmi = float(input("Enter the BMI Index: "))
if(bmi < 16):
    print("Severe Thinness")
elif (16 <= bmi <=17):
    print ("Moderate Thinness")
elif (17 < bmi <= 18.5):
    print ("Mild Thinness")
elif (18.5 < bmi <= 25):
    print ("Normal")
elif (25 < bmi <=30):
    print ("Overweight")
elif (30 < bmi <=35):
    print ("Obese class 1")
elif (35 < bmi <= 40):
    print ("Obese class 2")
else:
    print ("Obese class 3")