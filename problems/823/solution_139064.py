def faltante(lista_LN):
    a = [0] + lista_LN + [0]
    b = 0
    c = list(range(len(lista_LN)+1)) + [lista_LN] + [0]
    
    while b <= len(a):
        if c[b] != a[b]:
            return a[b-1]+'
        b += 1