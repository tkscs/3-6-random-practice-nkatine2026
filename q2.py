import random
animal = ["amphimbian", "mammal", "Reptile"]
ani = random.choice(animal)
age = ["4.20", "6.7", "6.9"]
a = random.choice(age)
color = ["orange", "black", "white"]
col = random.choice(color)
weight = ["Trump-sized", "normal-sized", "RFK Brain sized"]
we = random.choice(weight)
print(f"Your pet is a {ani}")
print(f"Your pet is {a} years old")
print(f"Your pet is {col}")
print(f"Your pet is {we}")