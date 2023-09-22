def faltante(numeros):
    '''
    Função que dado uma lista com os numeros de peças de um 
    tabuleiro faltando retorna o numero da peça faltante
    list--->int
    '''
    list.sort(numeros)
    if 1 not in numeros:
        return 1
    if numeros[-1] < len(numeros) + 1:
        return len(numeros) + 1
    n = 0
    peca = 0
    while n < len(numeros) - 1:
        if numeros[n + 1] - numeros[n] > 1:
            peca = peca + numeros[n] + 1
        n = n + 1
    return peca