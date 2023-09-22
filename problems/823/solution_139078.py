def faltante(lista):
    '''
    A soma de todos os números entre 1 e N se dá pela fórmula da soma da PA: N * (N + 1) / 2.
    Toma-se a soma da PA, e deste valor eu subtrai-se a soma dos elementos da lista.
    Recebe uma lista com inteiros e retorna um <int> o número que está faltando
    '''
    n = len(lista) + 1
    somatotal = n * (n + 1) // 2
    return somatotal - sum(lista)