def faltante(lista):
    '''função que dado uma lista de números inteiros de 1 a N, retorna
    o número inteiro deste intervalo que está faltando. lista -> int'''
    list.sort(lista)
    i= 0
    while i < len(lista):
        if lista[i] != i + 1:
            return i + 1  i += 1