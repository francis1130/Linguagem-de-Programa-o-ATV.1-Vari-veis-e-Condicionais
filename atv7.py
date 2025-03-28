n = int(input("Digite um número ímpar: "))
if (n % 2) != 0:
     na = n - 1 
     pn = n + 2 
     print(f"A diferença entre o quadrado do número anterior com o do próximo número ímpar é {(na**2) - (pn**2)}")
else: 
     print("Este número não é ímpar.")
