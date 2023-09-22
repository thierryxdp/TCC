def maiores(lista,n):
    '''funcao que recebe uma lista e um numero inteiro n 
    e retorna uma nova lista contendo apenas os numeros 
    maiores que n em ordem crescente; list,int -> list'''
    L = insere(lista,n)
    indice = list.index(L,n)
    del L[0:indice+1]
    return L