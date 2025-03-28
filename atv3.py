x = float(input("Digite o valor total das mercadorias compradas: "))
if x > 500: 
     ValorUlt = (x - 500)
     taxa = (ValorUlt/2) 
     print(f"O valor total de sua compra com o acréscimo dos impostos é: R${x + taxa}") 
else: 
     print("Sua compra não possui impostos.")
