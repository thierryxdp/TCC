def fatorial(num):
    '''Função que calculará o fatorial de um número. int -> int'''
    i=1
    l=list(range(num-1,0,-1))
    g=[num]
    while i<num:      
        if i>1:
            g[0]=g[0]*i
        i=i+1
    return g[0]