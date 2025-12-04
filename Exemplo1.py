#Listas
#São variáveis compostas para armazenamento de mais informações por vez
#É caracterizada no pytohn pelo []
#Por convenção, usamos o nome das listas no plural. É opcional o prefixo "list", "Lst"

list_meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho"]
print(list_meses[0])    #Primeiro
print(list_meses[-1])   #Último
print(list_meses[-2])   #Penúltimo
print(list_meses[1:4])  #Imprime a partir do indice 1 ao 3, porque começa no 0
print(list_meses[2:])   #Imprime a partir do indice 2 até o final
print(list_meses[:5])   #Imprime a partir do indice 0 até o 5-1
print(list_meses[0:6:2])   #De dois em dois, até o 6-1