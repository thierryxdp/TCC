def maiores(lista,n):
    '''
    Função que recebe uma lista e um número inteiro n e
    retorna outra lista que contém todos os numeros da lista 
    original maiores que n em ordem crescente.
    
    list->list
    '''
    lista.append(n)
    list.sort(lista)
    list.reverse(lista)
    i=lista[:list.index(lista,n)]
    list.reverse(i)
    return i