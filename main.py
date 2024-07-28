import xox
xoxmap = {"A1" : "_" , "A2" : "_" , "A3" : "_" , "B1" : "_" , "B2" : "_" , "B3" : "_" , "C1" : "_" , "C2" : "_" , "C3" : "_"}
gameModeMain = None
while True:
    print("Lütfen oynama istediğiniz modu seçini \n1- Klasik XOX\n2- XOX 2.0\n")
    gameModeMain = input(": ")
    if gameModeMain == "1" or gameModeMain == "2":
        xox.gameMode = int(gameModeMain)
        break
    elif gameModeMain.isnumeric() :
        print("Lütfen 1 veya 2 girin.")
    else :
        print("Lütfen sayısal bir değer giriniz")

while True : 

    xox.print_map(xoxmap )
    print("\n\n 1. Oyuncunun Sırası : ")
    xoxmap = xox.write_board(xoxmap , 1)
    
    if xox.is_finished(xoxmap ) :
        xox.print_map(xoxmap)
        print("\n\nOyun bitti !!! 1. Oyuncu kazandı tebrikler")
        break
    
    xox.print_map(xoxmap)
    print("\n\n 2. Oyuncunun Sırası : ")
    xoxmap = xox.write_board(xoxmap , 2)
    if xox.is_finished(xoxmap ) :
        xox.print_map(xoxmap)
        print("\n\nOyun bitti !!! 2. Oyuncu kazandı tebrikler")
        break
    
    
    