

def write_board(xoxmap): 
    
    while True : 
        line = input("Lütfen değiştireceğiniz sırayı alfabetik olarak giriniz : ").upper()
        if line not in ["A" ,  "B" , "C"] :            
            print("Hatalı sıra girdiniz lütfen yeniden giriniz")  
            continue
        collumn = input("Lütfen değiştireceğiniz sütunu numeric olarak giriniz : ") 
        if collumn.isnumeric():
                xoro = input("Lütfen değiştirmek istediğiniz karakteri giriniz X ya da O : ").upper()
                collumn = int(collumn)
                if 4 > collumn > 0: 
                    collumn = str(collumn)
                    square = line + (collumn)
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

    for i in lines :
         
         if (xoxmap[f"{i}1"]  + xoxmap[f"{i}2"] +  xoxmap[f"{i}3"]) == "XOX": 
              result = True
    for j in collumns:
         
         if (xoxmap[f"A{j}"] + xoxmap[f"B{j}"] + xoxmap[f"C{j}"]) == "XOX" : 
              result = True
    if (xoxmap["A1"] + xoxmap["B2"] + xoxmap["C3"]) == "XOX" or (xoxmap["A3"] + xoxmap["B2"] + xoxmap["C1"]) == "XOX":
         result = True
    return result