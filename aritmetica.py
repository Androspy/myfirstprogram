respuesta1 = input("te apetece un helado? Si o No: ")
respuesta2 = input("Tienes dinero para un helado? Si o No: ")
respuesta3 = input("Esta el señor de los helados? Si o No:  ")
respuesta4 = input("Está tu tía? Si o No:  ")



if respuesta1 == "Si" and (respuesta2 == "Si" or respuesta4 =="Si") and respuesta3 == "Si":
    print("comete un helado")
else:
    print("vete ya vago")