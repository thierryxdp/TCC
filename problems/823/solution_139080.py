def faltante (N):
    '''funçao que dada uma lista com numero inteiro 
    numerados de 1 a N, descubra qual numero inteiro 
    faltante no intervalo; list-> int'''
    i = 0
    s = []
    list.sort(N)
    while i<len(N)+1:
        s = s+[i+1]
        i = i+1
    a = sum(s)
    b = sum(N)
    return a-b