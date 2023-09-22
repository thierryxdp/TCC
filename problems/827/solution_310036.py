def qtd_divisores(n):
    r = []
    l 
    for i in list(range(0, n)):
        if n%i == 0:
            r.append(i)
    return len(r)