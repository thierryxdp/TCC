def qtd_divisores(n):
    r = []
    
    for i in list(range(1,n)):
        if n%i == 0:
            r.append(i)
    return r