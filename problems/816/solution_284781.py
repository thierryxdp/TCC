def maiores(lista,n):
    ''' se você me der uma lista de numeros inteiros e um numero inteiro n,
    retorno outra lista,com todos os numeros da lista origienal e em ordem 
    crescente.
    lista int -->lista int'''
    list(lista)
    lista.append(n)
    indN= lista.index(n)
    if n not in lista:
        lista.append(n)
    return lista[indN+1:]