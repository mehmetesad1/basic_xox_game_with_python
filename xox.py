gameMode = 2



def write_board(xoxmap , player = None): 
    
    while True : 
        if player == 1 : 
             print("Sıra 1. oyuncuda karakteri X")
        elif player == 2 : 
             print("Sıra 2. oyuncuda karakteri O")
        square = input("Lütfen değiştirmek istediğiniz karenin kordinatını  giriniz (örneğin : A1) : ").upper()
        line = square[0]
        collumn = square[1]
        if line not in ["A" ,  "B" , "C"] :            
            print("Hatalı sıra girdiniz lütfen yeniden giriniz")  
            continue       
        if collumn.isnumeric():
                if gameMode == 2 : 
                    xoro = input("Lütfen değiştirmek istediğiniz karakteri giriniz X ya da O : ").upper()
                elif gameMode == 1 :
                    if player == 1 :
                         xoro = "X"                        
                    elif player == 2 :
                         xoro = "O"
                collumn = int(collumn)
                if 4 > collumn > 0: 
                    
                    if xoxmap[square] == "_":
                        if xoro in ["X" , "O"] : 
                             xoxmap.update({square : xoro})
                             return xoxmap
                             break
                        else : 
                             print("Geçersiz karakter girdiniz lütfen X ya da O giriniz.") 
                             continue
                    else : 
                          print("Dolu bir kare girdiniz") 
                          continue
        else : 
             print("Hatalı sütun girdiniz lütfen yeniden giriniz.")       
             continue
        
def print_map(xoxmap): 
     lines = ["A" , "B" , "C" ]
     print("\t   1 2 3")
     for i in lines : 
          print(f"\t{i} |{xoxmap[f"{i}1"]}|{xoxmap[f"{i}2"]}|{xoxmap[f"{i}3"]}|")


def is_finished(xoxmap) : 
     lines = ["A" , "B" , "C"]
     collumns = ["1" , "2" , "3"]
     result = False
     if gameMode == 2 :
          for i in lines :
         
               if (xoxmap[f"{i}1"]  + xoxmap[f"{i}2"] +  xoxmap[f"{i}3"]) == "XOX": 
                    result = True

          for j in collumns:    

               if (xoxmap[f"A{j}"] + xoxmap[f"B{j}"] + xoxmap[f"C{j}"]) == "XOX" : 
                    result = True

          if (xoxmap["A1"] + xoxmap["B2"] + xoxmap["C3"]) == "XOX" or (xoxmap["A3"] + xoxmap["B2"] + xoxmap["C1"]) == "XOX":
               result = True

     elif gameMode == 1 : 
          for i in lines : 
               if (xoxmap[f"{i}1"]  + xoxmap[f"{i}2"] +  xoxmap[f"{i}3"]) == "XXX" or (xoxmap[f"{i}1"]  + xoxmap[f"{i}2"] +  xoxmap[f"{i}3"]) == "OOO": 
                    result = True
          for i in collumns :  
               if (xoxmap[f"A{i}"] + xoxmap[f"B{i}"] + xoxmap[f"C{i}"]) == "XXX" or (xoxmap[f"A{i}"] + xoxmap[f"B{i}"] + xoxmap[f"C{i}"]) == "OOO": 
                    result = True
          if (xoxmap["A1"] + xoxmap["B2"] + xoxmap["C3"]) == "XXX" or (xoxmap["A3"] + xoxmap["B2"] + xoxmap["C1"]) == "XXX":
               result = True
          if (xoxmap["A1"] + xoxmap["B2"] + xoxmap["C3"]) == "OOO" or (xoxmap["A3"] + xoxmap["B2"] + xoxmap["C1"]) == "OOO":
               result = True
     return result