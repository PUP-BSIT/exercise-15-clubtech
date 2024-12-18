import os
import time

class Dog:
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def show_all_menu(self):
        menu_exit = 6
        user_choice = 0 
        while user_choice != menu_exit:
            user_choice = self.display_menu()
            self.process_choice(user_choice)

    def display_menu(self):
        print("=================")
        print("Method Menu")
        print("1. Bark")
        print("2. Fetch")
        print("3. Sit")
        print("4. Run")
        print("5. Eat")
        print("6. Return to Main Menu")
        print("==================")
        user_input = int(input("Enter your choice: "))
        return user_input
            
    def process_choice(self,choices):
        match choices:
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
                time.sleep(2)
            case _:
                print("Incorrect choice")

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
   
def nolluda_object():
    dog_name = input("Enter your dog name: ")
    dog_breed = input("Enter the breed: ")
    dog_age = input("Enter the age: ")
    dog_1 = Dog(name=dog_name, breed=dog_breed, age=dog_age)
    os.system('cls')
    dog_1.show_all_menu()
    os.system('cls')

