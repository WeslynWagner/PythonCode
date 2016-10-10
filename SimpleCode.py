
    
name = input("Please enter your name:")
age = input("Pleae enter your age:")

def printName(name):
    print("Hi, your name is ", name)

def printAge(age):
    print("And your age is ", age)

evens_to_50 = [i**2 for i in range(51) if i %2 == 0]
print(evens_to_50)

printName(name)
printAge(age)
print(name[::-1])
