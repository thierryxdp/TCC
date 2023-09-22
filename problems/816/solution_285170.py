def maiores(lista, n):
    '''
    funcao que dada uma lista de numeros inteiros e um numero
    inteiro n, retorna outra lista que contem todos os numeros
    da lista original maiores que n, ordenados em ordem 
    crescente.
    lista---> list
    param n---> int
    return---> list
    '''
    list(lista)
    lista.append(n)
    ordenada = sorted(lista)
    indice = ordenada.index(n)
    
    if n not in ordenada:
        lista.append(n)
    return ordenada[indice+ 1:]