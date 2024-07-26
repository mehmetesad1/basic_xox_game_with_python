import xox
xoxmap = {"A1" : "_" , "A2" : "_" , "A3" : "_" , "B1" : "_" , "B2" : "_" , "B3" : "_" , "C1" : "_" , "C2" : "_" , "C3" : "_"}



while True : 
    xox.print_map(xoxmap)
    print("\n\n 1. Oyuncunun Sırası : ")
    xoxmap = xox.write_board(xoxmap)
    if xox.is_finished(xoxmap) :
        xox.print_map(xoxmap)
        print("\n\nOyun bitti !!! 1. Oyuncu kazandı tebrikler")
        break
    
    xox.print_map(xoxmap)
    print("\n\n 2. Oyuncunun Sırası : ")
    xoxmap = xox.write_board(xoxmap)
    if xox.is_finished(xoxmap) :
        xox.print_map(xoxmap)
        print("\n\nOyun bitti !!! 2. Oyuncu kazandı tebrikler")
        break
    
    
    