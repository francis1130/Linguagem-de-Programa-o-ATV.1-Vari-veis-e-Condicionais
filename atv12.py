t = int(input("Digite a quantidade de turmas da escola: "))
a = int(input("Em seguida, digite a quantidade total de alunos na escola: "))
m = a//t 
print(f"A média de alunos por turma é de: {m} ")
if m > 40:
     print("Há alguma(s) turma(s) com mais de 40 alunos.")
