# Insere Ordenado
def insere(lista_numero, n):
    '''Essa função recebe uma lista de números e um outro número o qual ela deverá
    inserir na lista de modo que esta continue ordenada
    LIST, FLOAT -> LIST'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero