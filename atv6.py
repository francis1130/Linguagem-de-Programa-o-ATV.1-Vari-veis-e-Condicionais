def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def gerar_primos(n):
    primos = []
    num = 2
    while len(primos) < n:
        if eh_primo(num):
            primos.append(num)
        num += 1
    return primos

# Exibe os 100 primeiros números primos
primos = gerar_primos(100)
print(primos)
