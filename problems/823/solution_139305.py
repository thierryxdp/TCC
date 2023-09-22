def faltante(N):
    """funcao que dada uma lista com N - 1 inteiros numerados de 1 a N, descobre qual o 
    numero inteiro do intervalo ta faltando"""
    i = 0
    s = []
    list.sort(N)
    while i < len(N) + 1:
        s = s + [i+1,]
        i = i + 1
    a = sum(s)
    b = sum(N)
    return a - b