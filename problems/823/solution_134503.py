def faltante(lista_pecas):
    '''Função que recebe uma lista de N - 1 termos, a qual
    N simboliza o número de peças de um quebra-cabeça e verifica
    qual a peça que está faltando neste quebra-cabeça.
    [list] -> int'''
    i = 1
    while i < len(lista_pecas):
        if lista_pecas[i] != lista_pecas[i-1] + 1:
            return lista_pecas[i] - 1    
        i = i + 1
        
    if lista_pecas[0] != 1:
        return 1
    
    return len(lista_pecas) + 1