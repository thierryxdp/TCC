def faltante(lista):
    '''Função que dado uma lista de números inteiros de 1 a N, retorna o número inteiro deste intervalo que está faltando'''
    list.sort(lista)
    w = 0
    while w < len(lista):
        if lista[w] != w + 1:
            return w + 1
        w += 1