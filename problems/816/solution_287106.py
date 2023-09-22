def maiores (lista,n):
    '''Função de dada uma lista, retorna outra lista coms os nº maiores que n em ordem crescente.
    list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    i = list.index(lista,n) 
    return lista[i+1:]