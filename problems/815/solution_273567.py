def insere(lista_de_numero,n):
    '''Você me dando uma lista de numeros inteiros e um numero inteiro n 
    vou incluir este numero numa posição correta'''
    lista_de_numero.append(n)
    lista_de_numero.sort()
    return lista_de_numero