def faltante(lista_pecas):
    '''Função que retorna o número da peça
    faltante.
    Dados de entrada: list
    Valor de saída: int
    '''
    pecas = len(lista_pecas) + 1
    i = 0
    while i < pecas:
        if i + 1 not in lista_pecas:
            return i + 1
        if lista_pecas[1] != i + 1:
            return i + 1
        else:
            return i + 1