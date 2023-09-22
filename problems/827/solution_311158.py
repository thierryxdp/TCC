def filtra (ls, p):
    r = []
    for e in ls:
        if p(e):
            r.append(e)
    return r

def qtd_divisores(n):
        
    r = range(1, n+1)
    
    return len(filter(r, lambda x: n%x == 0))