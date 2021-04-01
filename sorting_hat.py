import random

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

name = input("What's your name? ")

answer = (input("Which of the following best describes you? A) Brave & Helpful   B) Patient & Loyal   C) Intellligent & Witty   D) Ambitious & Cunning : d")).upper()

if answer == "A":
    match = "Gryffindor"
elif answer == "B":
    match = "Hufflepuff"
elif answer == "C":
    match = "Ravenclaw"
elif answer == "D":
    match = "Slytherin"
else: 
    match = random.choice(houses)

print(name + "..." + "hmmm...." + "you are indubitably of the House of " + match)

