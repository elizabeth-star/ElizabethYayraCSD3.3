depositor={"0243454545":{"c":"Yayra", "b":2300,"n":"3434"},

"0543535353":{"s":"betty", "k":430, "l": "5678"},

"0244342434":{"h":"liz", "t":3457, "y": "1890"}

}

def cashier():
    Pole = input("pin: ")
    cod = depositor["0243454545"]["n"]
    if Pole == cod:
       kim = input("name: ")
       hot = depositor["0243454545"]["c"]
    if kim == hot:
   
       job = input("amount: ")
    
    if job >="1":
       sol = input("comfirm pin: ")
    if sol == cod:
        print("Transaction successful")
    else:
        print("enter pin again")  
       

cashier()





    




