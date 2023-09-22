def faltante(pecinhas: list) -> int:
    '''Dada uma lista de peças de 1 a N e tamanho N-1, 
    devolve o número da pecinha faltante'''
    i = 1
    list.sort(pecinhas)
    while (i < len(pecinhas) - 1) and not(pecinhas[i] != pecinhas[i - 1] + 1):
        i += 1
    num_pecinha = pecinhas[i] - 1
    return num_pecinha