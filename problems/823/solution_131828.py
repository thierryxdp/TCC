def faltante(lista):
    '''Função que dado uma lista de números inteiros de 1 a N, retorna o número inteiro deste intervalo que está faltando'''
    list.sort(lista)
    x = 0
    while x < len(lista):
        if lista[x] != x + 1:
            return x + 1
        else:
            return len(lista)+1