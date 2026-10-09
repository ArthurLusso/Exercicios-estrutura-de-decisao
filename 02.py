estudante = input ("Você é estudante? (sim/não) ")
dia_da_semana = input ("Qual o dia da semana? (terça/outro) ")
sala = input ("Qual tipo de sala? (VIP/comum)" )

if (estudante == "sim") or (dia_da_semana == "terça") and (sala == "comum"):
    print ("Desconto aplicado")

else:
    print ("Valor Integral")