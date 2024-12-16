import os
import time

class Dog:
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f"The {self.breed}, dog named {self.name}"
        f" {self.age} years old, is barking ")
    
    def fetch(self):
        print(f"The {self.breed}, dog named {self.name}"
        f" {self.age} years old, is fetching")
    
    def sit(self):
        print(f"The {self.breed}, dog named {self.name}"
        f" {self.age} years old, is sitting")
    
    def run(self):
        print(f"The {self.breed}, dog named {self.name}"
        f" {self.age} years old, is running")
    
    def eat(self):
        print(f"The {self.breed}, dog named {self.name}"
        f" {self.age} years old, is eating")
    
    def menu(self):
        while True:
            print("===============")
            print("Dog Actions")
            print("1. Bark")
            print("2. Fetch")
            print("3. Sit")
            print("4. Run")
            print("5. Eat")
            print("6. Return to Main Menu")
            print("===============")
            user_input = int(input("Enter your choice: "))
        
            match user_input:
                case 1:
                    self.bark()
                case 2:                    
                    self.fetch()
                case 3:                
                    self.sit()
                case 4:
                    self.run()
                case 5:
                    self.eat()
                case 6:
                    print("Returning to Main Menu...")
                    time.sleep(3)
                    break
                case _:
                    print("Incorrect choice")

def nolluda_object():
    dog_name = input("Enter your dog name: ")
    dog_breed = input("Enter the breed: ")
    dog_age = input("Enter the age: ")
    dog_1 = Dog(name=dog_name, breed=dog_breed, age=dog_age)
    os.system('cls')
    dog_1.menu()
    os.system('cls')

