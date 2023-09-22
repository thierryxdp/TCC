def faltante(lista):
    '''Função que retorna qual o número inteiro deste intervalo está faltando, list, int -> int'''
    x = 0
    peca = []
    while x<len(lista):
        peca = peca[x] - 1
        x = x - 1
    return peca