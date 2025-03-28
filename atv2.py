T  = int(input("Digite um tempo em segundos: "))
min = (T/60)
hrs = (min/60)
dias = (hrs//24)

print(f"Equivale a {dias} dia(s), {hrs} horas e {min} minutos.")
