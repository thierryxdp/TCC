def faltante(lista_numeros):
    '''
    dada uma lista de numeros inteiros em sequencia,
    retorna o inteiro faltante
    dados de entrada: list:
    retorna: int
    '''
    contador = 0
    while contador < len(lista_numeros):
        if lista_numeros[contador] != contador + 1:
            return contador + 1
        contador = contador + 1