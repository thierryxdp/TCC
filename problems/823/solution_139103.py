def faltante (lista):
    '''Retorna qual peça está faltando dentre uma lista de peças numeradas de 1 a N
    list->int'''
    peca = []
    for element not in lista:
        if element > 0 and element < len(lista):
            peca.append (element)
    return peca