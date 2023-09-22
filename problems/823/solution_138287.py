def faltante(pecas):
    '''Função que, dada uma lista com N - 1 inteiros
    numerados de 1 a N, retorna qual número inteiro 
    deste intervalo está faltando
    list -> int'''
    valores = sorted(pecas)
    for x in range(len(valores)):
        if x + 1 != valores[x]:
            return x + 1
    return len(valores) + 1