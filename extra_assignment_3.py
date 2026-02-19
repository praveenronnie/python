# Correct or wrong 
num = int(input("Enter the value: "))
if num == 10:
    print('corrent')
else:
    print('Incorrect')
print('\n')   

# Check password
passKey = 'HOPE@123'
password = str(input("Enter your password: "))
if password == passKey:
    print("Your password is correct")
else:
    print("Your password is incorrect")
print('\n')

# Catagory the people by their age like children, adult, citizen, senior citizen..
age = int(input("Enter your age: "))
if 0 < age < 12:
    print("Children")
if 12 < age <= 17:
    print("Teen")
elif 17 < age <= 30:
    print("Adult")
elif 30 < age <= 60:
    print("Citizen")
else:
    print("Senior Citizen")
print('\n')

# Find whether number is positive or negative
num = int(input("Enter the number: "))
print("Postive" if num > 0 else "negative" if num < 0 else "Zero")
print('\n')

# Check whether the number is divisible by 5
num = int(input("Enter the number: "))
print ("Divisible by 5" if num % 5 == 0 else "Not Divisible by 5")