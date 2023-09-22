def faltante(lista_pecas):
    '''Função que recebe uma lista de N - 1 termos, a qual
    N simboliza o número de peças de um quebra-cabeça e verifica
    qual a peça que está faltando neste quebra-cabeça.
    [list] -> int'''
    lista_pecas_ordenadas = list.sort(lista_pecas)
    i = 1
    while i < len(lista_pecas_ordenadas):
        if lista_pecas_ordenadas[i] != lista_pecas[i-1] + 1:
            return lista_pecas_ordenadas[i] - 1
        i = i + 1