# Dada uma lista e um inteiro n, esta função retorna uma nova lista ordenada, 
# contendo os elementos da original que são maiores do que n.
# list, int -> list

def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    
    return lista[indice+1:]