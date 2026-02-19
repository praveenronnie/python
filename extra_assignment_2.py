# Print Range
for i in range(0, 21):
    print(i)

# Print range from 10 to 20
print(list(range(10, 20)))

# Print No.of items in list
items = [10, 20, 14, 55, 43, 87, 76]
print("Number of items in the list is: ", len(items))

# Print Sentence
text = 'Artificial Intelligence'
for char in text:
    print(char)

# Get Inputs
name = str(input("-YOUR NAME-"))
age = str(input("-YOUR AGE-"))
profession = str(input("-YOUR PROFESSION-"))
print(name + " " + age + " " + profession)
print('\n')

# Print Tuple
tup = (1, 'Welcome', 2, 'Hope')
print(tup)

# Print ODD numbers
tup1 = (20, 10, 16, 19, 25, 1, 276, 188)
for num in tup1:
    if num & 1:
        print(num)
print('\n')

# Print Even numbers
tup1 = (20, 10, 16, 19, 25, 1, 276, 188)
for num in tup1:
    if (num & 1) != 1:
        print(num)