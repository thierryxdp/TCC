def faltante(lista):
    '''Função que retorna qual o número inteiro deste intervalo está faltando, list, int -> int'''
    x = 0
    peca = []
    while (lista>=1):
        lista = lista[x] - 1
        x = x - 1
    return peca