n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

medArit = (n1 + n2 + n3)/3
medPond1 = ((n1*2) + (n2*2) + (n3*3))/7
medPond2 = ((n1*1) + (n2*2) + (n3*3))/6

print(f"A média aritmética é: {medArit}")
print(f"A primeira média ponderada é: {medPond1}")
print(f"A segunda média ponderada é: {medPond2}")
