respuesta1_input = input("te apetece un helado?").upper()
if respuesta1_input == "SI":
    respuesta1_reload = True
elif respuesta1_input == "NO":
    respuesta1_reload == False
else:
    print("opción invalida, seguro no quieres helado")
    respuesta1_reload = False

respuesta2_input = input("tienes dinero?").upper()
respuesta3_input = input("está el señor de los helados?").upper()
respuesta4_input = input("está tu tía?").upper()

respuesta1_reload = respuesta1_input == "SI"
respuesta2_reload = respuesta2_input == "SI" or respuesta4_input == "SI"
respuesta3_reload = respuesta3_input == "SI"

if respuesta1_reload and respuesta2_reload and respuesta3_reload:
    print("comete un helado")
else:
    print("Largo de aqui, maldito cerdo")