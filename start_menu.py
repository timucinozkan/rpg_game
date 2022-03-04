# Opening Menu func

def first_screen():
    print('\n\nLutfen secimini yap')
    while True:
        start_menu_selection = input('1 - Yeni Oyun\n2 - Eski Maceraya Don\n3 - Cikis Yap\n\n\n>>>')
        try:
            start_menu_selection == int(start_menu_selection)
            break
        except:
            print("Dogru bir secim yaptigina emin misin? Bence tekrar dene!!")
    return start_menu_selection