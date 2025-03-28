n1= float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
if n1 > n2 > n3: 
     print(f"Esse é o maior número: {n1}")
     print(f"Esse é o menor número: {n3}")
elif n1 > n3 > n2: 
     print(f"Esse é o maior número: {n1}")
     print(f"Esse é o menor número: {n2}")
elif n2 > n1 > n3: 
     print(f"Esse é o maior número: {n2}")
     print(f"Esse é o menor número: {n3}")
elif n2 > n3 > n1: 
     print(f"Esse é o maior número: {n2}")
     print(f"Esse é o menor número: {n1}")
elif n3 > n2 > n1: 
     print(f"Esse é o maior número: {n3}")
     print(f"Esse é o menor número: {n1}")
else: 
     print(f"Esse é o maior número: {n3}")
     print(f"Esse é o menor número: {n2}")
