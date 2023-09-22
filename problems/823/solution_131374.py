def faltante(listaPecas):
    n = len(listaPecas) + 1
    somatotal = n * (n+1)//2
    return somatotal - sum(listaPecas)