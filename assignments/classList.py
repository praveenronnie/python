class SubFields():
    
    def subFieldsInAi():
        fields = ["Machine Learning", 
        "Neural Networks",
        "Vision", "Robotics", 
        "Speech Processing", 
        "Natural Language Processing"]
        print("SubFields in AI are: ")
        for field in fields:
            print(field)

class OddEven():
    def oddOrEven():
        num =int(input("Enter the Number: "))
        if(num % 2 == 0):
            print("even")
        else:
            print("Odd")


class MarriageEligibility():
    def eligibility():
        age = int(input("YOUR AGE: "))
        gender = str(input("YOUR GENDER: ").lower())
        if(gender == "male" and age>20) or (gender == 'female' and age > 17):
            print('Eligible')
        else:
            print('Not Eligible')


class Percentage():
    def findPercentage():
        marks = []
        totalSubjects = int(input("Enter total number of Subjects: "))
        for i in range (1, totalSubjects + 1):
            sub = int(input(f"Subject {i} = "))
            marks.append(sub)
        print("Total: ", sum(marks))
        print("Percentage: ", sum([x for x in marks])/ len(marks))


class Triangle():
    def areaOfTraingle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))
        area = (height * breadth) / 2
        print("Area of Traingle: " +  str(area))
        
    def perimeterOfTraingle():
        h1 = float(input("Height1: "))
        h2 = float(input("Height2: "))
        b = float(input("Breadth: "))
        print("Perimeter of Traingle: " +  str(h1 + h2 + b))
    
    

        