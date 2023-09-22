# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """"""
lista_ordenada = []
tam = len(lista)
for i in range(tam):
 menor = lista[0]
 for j in range(len(lista)):
 if lista[j] < menor:
 menor = lista[j]
 pos_menor = j
 lista_ordenada.append(menor)
 lista.remove(menor)
return(ista_ordenada)