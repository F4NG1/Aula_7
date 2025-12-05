#Dicionário
#Estrutura chave e valor
#Símbolo {}

# notas={} #Dicionário vazio
# notas['Matemática']=8.5
# notas['Português']=7.0
# notas['História']=9.2
# notas['Matemática'] = 8.0
# notas['Geografia'] = 9.9
# del notas['História']
# print(notas)

livro={}
lista_cadastro=[]

#Cadastro em Dicionários

for i in range(3):
    titulo=input('informe o Título: ')
    autor=input('informe o Autor: ')
    ano=input('informe o Ano: ')
    genero=input('informe o Gênero: ')

    livros={
        'Título': titulo,
        'Autor': autor,
        'Ano': ano,
        'Gênero': genero
    }
    
    lista_cadastro.append(livros)
    print(f'{i+1} Livros Cadastrados ')
print()
print(lista_cadastro)