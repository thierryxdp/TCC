def insere(lista_numero,n):
    '''funcao que recebe uma lista e um numero inteiro
 e retorna uma nova lista contendo o novo numero em
 ordem crescente; list,int -> list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    '''funcao que recebe uma lista e um numero inteiro n e 
    retorna uma nova lista contendo apenas os elementos 
    maiores que n em ordem crescente; list,int -> list'''
    L = insere(lista,n)
    indice = list.index(L,n)
    del L[0:indice+1]
    return L