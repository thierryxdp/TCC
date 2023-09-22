def faltante(lista_pecas):
    '''Função que retorna o número da peça
    faltante.
    Dados de entrada: list
    Valor de saída: int
    '''
    pecas = len(lista_pecas)+1
    list.sort(lista_pecas)
    indice = 0
    while indice < pecas:
        if indice+1 not in lista_pecas:
            return indice+1
        if lista_pecas[1] != indice+1:
            return indice+1
        else:
            return indice+1