def maiores(lista, n):
    '''
    funcao que dada uma lista de numeros inteiros e um numero
    inteiro n, retorna outra lista que contem todos os numeros
    da lista original maiores que n, ordenados em ordem 
    crescente.
    :param lista: list
    :param n: int
    :return: list
    '''
    list(lista)
    lista.append(n)
    lista_ordenada = sorted(lista)
    indice_n = lista_ordenada.index(n)
    
    if n not in lista_ordenada:
        lista.append(n)
    return lista_ordenada[indice_n + 1:]