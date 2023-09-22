def faltante(lista):
    '''Função que dada uma lista com inteiros numerados de 1 a N, retorna qual número inteiro deste intervalo está faltando: list -> int'''
    i = 0
    while i < len(lista):
        if i != lista[i]-1:
            faltante = i+1
            return faltante
        i += 1