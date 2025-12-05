lista_numeros=[]

for n in range(5):
    num=float(input('Informe o número: '))
    lista_numeros.append(num)

print(lista_numeros[0])
lista_numeros[0]=22 #Altera a posição 0
lista_numeros.pop() #Deleta o último
lista_numeros.remove(30) #Deleta pelo valor
#del lista_numeros[0]
print(lista_numeros)