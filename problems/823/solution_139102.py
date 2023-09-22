def faltante(lista):
    """funcao que dada uma lista com N-1 inteiros
    numerados de 1 a N, retorna qual numero inteiro
    deste intervalo esta faltando
    list->int"""
    n = len(lista)
    x = (n+1)*(n+2)//2
    return x - sum(lista)