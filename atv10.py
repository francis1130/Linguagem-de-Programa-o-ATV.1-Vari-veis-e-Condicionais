def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita um número do usuário
while True:
    try:
        num = int(input("Digite um número inteiro maior que 1: "))
        if num > 1:
            break
        else:
            print("O número deve ser maior que 1.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Verifica se é primo
if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
