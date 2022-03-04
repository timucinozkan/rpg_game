from intro import welcome
from start_menu import first_screen
from new_game import new_game

welcome()
while True: 
    menu_selection = first_screen()
    try:
        if menu_selection == "1" :
            new_game()
            break
        elif menu_selection == "2" :
            None
            break
        elif menu_selection == "3" :
            print('Peki, baska zaman gorusuruz')
            exit
        else:
            print("Hmm, oyle bir secenek yok farketmediysen! Tekrar deneyelim.\n")
    except:
        print("Noldu oyle?")

