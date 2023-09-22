def repetidos (lista):
    """ funcao ira receber uma lista e retornara o numero de vezes que um elemento da lista é igual ao elemento anterior
    entrada: lista   saida: int"""
    i = 0
    repetidos = 0
    while i < len (lista):
        if lista [i] == lista [i - 1]:
            repetidos = repetidos + 1
        i = i + 1
        if len (lista) == 2 and lista[0] == lista [1]:
            repetidos = 1
    return repetidos