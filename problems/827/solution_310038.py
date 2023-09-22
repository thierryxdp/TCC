def qtd_divisores(n):
    r = []
    
    for i in list(range(n)):
        if n%i == 0:
            r.append(i)
    return len(r)