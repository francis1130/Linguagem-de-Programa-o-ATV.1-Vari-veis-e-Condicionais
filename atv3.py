d = int(input("Quantos dias você passou com o carro? "))
taxaD = (d * 90)

km = int(input("Quantos quilômetros você percorreu com este carro? "))
if km > 100: 
     kmAd = (km - 100)
     taxaK = (kmAd * 12)
     print(f"O valor total do aluguel é R${taxaD +taxaK}.")
else: 
     print(f"O valor total do aluguel é de R${taxaD}.")
