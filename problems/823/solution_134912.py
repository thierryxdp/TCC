def faltante(lista):
    '''Função que dada uma lista com inteiros numerados de 1 a N, retorna qual número inteiro deste intervalo está faltando: list -> int'''
    i = 0
    while i < len(lista):
        if lista[i] in lista:
            i += 1
        if lista[i] not in lista:
            return lista[i]