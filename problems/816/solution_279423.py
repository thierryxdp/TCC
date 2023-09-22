def maiores(lista_de_numeros, n):
    '''compara os numeros da lista fornecida com n e retorna todos que são maiores, organizados do menor para
    o maior.
    list->list'''
    lista_resultado = []
    for numero in lista_de_numeros:
        if numero > n:
            lista_resultado.append(numero)
    lista_resultado.sort()
    return lista_resultado