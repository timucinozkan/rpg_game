# Opening Menu func

def first_screen():
    print('\n\nLütfen seçimini yap')
    while True:
        start_menu_selection = input('1 - Yeni Oyun\n2 - Eski Maceraya Dön\n3 - Çıkış Yap\n\n\n>>> ')
        
        if start_menu_selection.isdigit():  # Check if input is a number
            selection = int(start_menu_selection)
            if selection in [1, 2, 3]:  # Validate the selection
                return selection
            else:
                print("Seçiminiz 1, 2 veya 3 olmalı. Lütfen tekrar deneyin.")
        else:
            print("Lütfen geçerli bir sayı girin.")