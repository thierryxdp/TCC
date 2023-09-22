def fatorial(n):
    '''Função que, dado um número, calcule seu fatorial.
    int --> int'''
    i = 1
    resposta = 1
    while i <= n:
        resposta = resposta*i
        i = i + 1
    return resposta