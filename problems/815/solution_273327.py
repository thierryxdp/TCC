def insere(lista_numero,n):
    '''
    Coloca uma lista em ordem crescente
    entrada:int
    saida:int
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero