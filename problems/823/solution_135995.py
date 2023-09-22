def faltante(lista):
    s=0
    p = 0
    while p < (len(lista)+1):
        p = p + 1
        s=s+(1+p)
    return s-sum(lista)