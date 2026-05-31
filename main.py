import json
import random
from datetime import datetime

# Load data from tips.json
with open("tips.json", "r") as file:
    data = json.load(file)

name = input("Enter your name: ")
print(f"\nWelcome, {name}!")

while True:
    print("\n===== SMART STUDENT ASSISTANT =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = random.choice(data["study_tips"])

    elif choice == "2":
        result = random.choice(data["motivation_quotes"])

    elif choice == "3":
        result = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    elif choice == "4":
        print("Thank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid Choice!")
        continue

    print("\n" + result)

    with open("output.txt", "a") as file:
        file.write(result + "\n")
