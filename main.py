from clubtech import arroyo, nolluda, lazaro
import time
import os

while True:
    print("============")
    print("MAIN MENU (CLUBTECH)")
    print("============")
    print("1. John Matthew Arroyo")
    print("2. Franco Alfonso Lazaro")
    print("3. John Carlo Nolluda")
    print("4. Exit")
    print("==========================")
    user_choice = int(input("Enter your choice: "))

    match user_choice:
        case 1:
            os.system('cls')
            arroyo.arroyo_object()
        case 2:
            os.system('cls')
            lazaro.lazaro_object()
            pass
        case 3:
            os.system('cls')
            nolluda.nolluda_object()
        case 4:
            print("Bye Bye!")
            break
        case _:
            print("Incorrect choice (Pick 1 - 4 only)")
            

