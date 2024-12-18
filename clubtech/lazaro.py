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

class Anime:
    
    def __init__(self, name, director, episodes):
        self.name = name
        self.director = director
        self.episodes = episodes
    
    def display_all(self):
        menu_exit = 6
        user_choice = 0 
        while user_choice != menu_exit:
            user_choice = self.display_menu()
            self.process_choice(user_choice)
            
    def display_menu(self):
        print("----------------")
        print("Anime Menu")
        print("1. Show Anime Name")
        print("2. Show Anime Director")
        print("3. Show Number of Episodes")
        print("4. Anime Ratings")
        print("5. Write Message")
        print("6. Exit")
        print("----------------")
        user_input = int(input("Enter your choice: "))
        return user_input
            
    def process_choice(self, choices):
        match choices:
            case 1:
                choice_sound()
                self.show_name()
            case 2:
                choice_sound()
                self.show_director()
            case 3:
                choice_sound()
                self.show_episodes()
            case 4:
                choice_sound()
                self.show_ratings()
            case 5:
                os.system('cls')
                choice_sound()
                self.give_message()
            case 6:
                choice_exit_sound()
                print("Exiting the menu...")
                time.sleep(2)
            case _:
                choice_exit_sound()
                print("Invalid choice")
    
    def show_name(self):
        print(f"Anime Name: {self.name}")
    
    def show_director(self):
        print(f"Anime Director: {self.director}")
    
    def show_episodes(self):
        print(f"Number of Episodes: {self.episodes}")

    def show_ratings(self):
        if self.episodes > 500:
            print(f"This anime, {self.name}, is very popular!")
        elif self.episodes < 500 and self.episodes > 100:
            print(f"This anime, {self.name}, is popular!")
        elif self.episodes < 100 and self.episodes > 20:
            print(f"This anime, {self.name}, is average")
        else:
            print(f"This anime, {self.name}, is bad. It might not have any"
                  " additional seasons")
            
    def give_message(self):
        user_message = (input("Enter your message: "))
        print(f"Thank you! your ratings has been delivred to"
                      f" {self.director} sensei")
        print("*************")
        print(user_message)
        print("*************")

def get_episode():
    while True: 
        try:
            anime_episodes = int(input("Enter the number of episodes: "))
            if anime_episodes <= 0:
                print("Please enter a positive number.")
                continue  
            return anime_episodes  
        except ValueError:
            print("Invalid input! Please enter a valid number for episodes.")

def lazaro_object():
    anime_name = input("Enter the anime name: ")
    anime_director = input("Enter the anime director: ")
    anime_1 = Anime(name=anime_name, director=anime_director, 
                    episodes=get_episode())
    os.system('cls')
    anime_1.display_all()
    os.system('cls')
    