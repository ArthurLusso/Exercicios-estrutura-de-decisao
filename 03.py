renda = float(input("Digite sua renda: "))
score = int(input("Digite seu score:  (até 1000)"))
bens = input("Você possui algum tipode bem como garantia? (sim ou não)")
inadimplência = input("Você é inadimplente? (sim ou não)")

if (renda >= 3000) and (score >= 600) and (inadimplência == "nao") or (inadimplência == "nao") and (bens == "sim"):
    print(f"Emprestimo Aprovado!")

else:
    print(f"Emprestimo Negado!")

