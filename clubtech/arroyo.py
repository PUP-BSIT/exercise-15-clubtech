import os
import time
import winsound

SOUND_FREQUENCY = 300
MIN_SOUND = 150
MAX_SOUND = 300

def choice_sound():
    winsound.Beep(SOUND_FREQUENCY, MIN_SOUND)

def choice_exit_sound():
    winsound.Beep(SOUND_FREQUENCY, MAX_SOUND)

class Car:
    
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
    
    def display_all_menu(self):
        menu_exit = 6
        user_choice = 0 
        while user_choice != menu_exit:
            user_choice = self.display_menu()
            self.process_choice(user_choice)

    def display_menu(self):
        print("----------------")
        print("Method Menu")
        print("1. Move the car")
        print("2. Stop the car")
        print("3. Accelerate the car")
        print("4. Decelerate the car")
        print("5. Back up the car")
        print("6. Return to Main Menu")
        print("-----------------")
        user_input = int(input("Enter your choice: "))
        return user_input
            
    def process_choice(self,choices):
        match choices:
            case 1:
                choice_sound()
                self.drive_move()
            case 2:
                choice_sound()
                self.drive_stop()
            case 3:
                choice_sound()
                self.drive_accelerate()
            case 4:
                choice_sound()
                self.drive_decelerate()
            case 5:
                choice_sound()
                self.drive_back_up()
            case 6:
                choice_exit_sound()
                print("Returning to Main Menu...")
                time.sleep(2)
            case _:
                choice_exit_sound()
                print("Incorrect choice")
    
    def drive_move(self):
        print(f"This {self.year}, color {self.color}"
        f" {self.model} car is moving")
    
    def drive_stop(self):
        print(f"This {self.year}, color {self.color}"
        f" {self.model} car is stopped")
    
    def drive_accelerate(self):
        print(f"This {self.year}, color {self.color}"
        f" {self.model} car is accelerating")
    
    def drive_decelerate(self):
        print(f"This {self.year}, color {self.color}"
        f" {self.model} car is decelerating")
    
    def drive_back_up(self):
        print(f"This {self.year}, color {self.color}"
        f" {self.model} car is backing up")
   
def arroyo_object():
    car_model = input("Enter your car model: ")
    car_year = input("Enter the car's year of creation: ")
    car_color = input("Enter the car color: ")
    car_1 = Car(model=car_model, year=car_year, color=car_color)
    os.system('cls')
    car_1.display_all_menu()
    os.system('cls')

