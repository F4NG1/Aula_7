list_notas=[]

for n in range(5):
    nota=float(input('Informe a nota: '))
    list_notas.append(nota)

for n in list_notas:
    if n>=7:
        print(n); print('Aprovado')
    else:
        print('Reprovado')
