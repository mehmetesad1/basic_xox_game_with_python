import xox
xoxmap = {"A1" : "_" , "A2" : "_" , "A3" : "_" , "B1" : "_" , "B2" : "_" , "B3" : "_" , "C1" : "_" , "C2" : "_" , "C3" : "_"}



while True : 
    print("\t   1 2 3")
    print(f"\tA |{xoxmap["A1"]}|{xoxmap["A2"]}|{xoxmap["A3"]}|")
    print(f"\tB |{xoxmap["B1"]}|{xoxmap["B2"]}|{xoxmap["B3"]}|")
    print(f"\tC |{xoxmap["C1"]}|{xoxmap["C2"]}|{xoxmap["C3"]}|")
    print("\n\n 1. Oyuncunun Sırası : ")
    xoxmap = xox.print_board(xoxmap)
    if xox.is_finished(xoxmap) :
        print("\t   1 2 3")
        print(f"\tA |{xoxmap["A1"]}|{xoxmap["A2"]}|{xoxmap["A3"]}|")
        print(f"\tB |{xoxmap["B1"]}|{xoxmap["B2"]}|{xoxmap["B3"]}|")
        print(f"\tC |{xoxmap["C1"]}|{xoxmap["C2"]}|{xoxmap["C3"]}|")
        print("\n\nOyun bitti !!! 1. Oyuncu kazandı tebrikler")
        break
    
    print("\t   1 2 3")
    print(f"\tA |{xoxmap["A1"]}|{xoxmap["A2"]}|{xoxmap["A3"]}|")
    print(f"\tB |{xoxmap["B1"]}|{xoxmap["B2"]}|{xoxmap["B3"]}|")
    print(f"\tC |{xoxmap["C1"]}|{xoxmap["C2"]}|{xoxmap["C3"]}|")
    print("\n\n 2. Oyuncunun Sırası : ")
    xoxmap = xox.print_board(xoxmap)
    if xox.is_finished(xoxmap) :
        print("\t   1 2 3")
        print(f"\tA |{xoxmap["A1"]}|{xoxmap["A2"]}|{xoxmap["A3"]}|")
        print(f"\tB |{xoxmap["B1"]}|{xoxmap["B2"]}|{xoxmap["B3"]}|")
        print(f"\tC |{xoxmap["C1"]}|{xoxmap["C2"]}|{xoxmap["C3"]}|")
        print("\n\nOyun bitti !!! 2. Oyuncu kazandı tebrikler")
        break
    
    
    