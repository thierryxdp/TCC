def mapeia(ls,f):
    r=[]
    for e in ls:
        r.append(f(e))
    return r

def qtd_divisores(n):
    '''int > int
    Conta a quantidade de divisores que um número n tem'''
    
    r = range[1, n+1]
    
    return len(mapeia(r, lambda x: n%x == 0))