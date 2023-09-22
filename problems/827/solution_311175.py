def filtra (ls, p):
    r = []
    for e in ls:
        if p(e):
            r.append(e)
    return r

def qtd_divisores(n):
    '''int > int
    Conta a quantidade de divisores que um número n tem'''
    
    r = range(1, n+1)
    
    return len(filtra(r, lambda x: n%x == 0))