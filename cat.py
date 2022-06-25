#create class to catagorize information
class Cat: #function to interperate information 
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Chuck", 2)
cat2 = Cat("Jumper", 1)
cat3 = Cat("Bilbo", 4)

# 2 Create a function that finds the oldest cat
def max_age():
    old = max(cat1.age, cat2.age, cat3.age)
    return old

old_cat = max_age()

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {old_cat} years old.")