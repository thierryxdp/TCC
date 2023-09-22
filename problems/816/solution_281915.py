def maiores(lista,n):
    '''
    Função que recebe uma lista e um número inteiro n e
    retorna outra lista que contém todos os numeros da lista 
    original maiores que n em ordem crescente.
    
    list->list
    '''
    lista.append(n)
    lista.sort()
    i=lista[lista.index(n)+1:]
    return i