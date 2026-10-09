idade = float(input("Qual a sua idade? "))
altura = float(input("Qual a sua altura? "))
autorizacao_dos_pais = input("Você tem altorização dos pais? (sim ou não)")

if (idade >= 12) and (altura >= 140) or (autorizacao_dos_pais == "sim"):
    print (f"Você está liberado")

elif (idade < 12) and (altura < 140):
    if (autorizacao_dos_pais == "sim"):
        print (f"Você está liberado")

    elif (autorizacao_dos_pais == "não"):
        print ("Você não está liberado")
         


 

