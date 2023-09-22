def qtd_divisores(numero):
    n = 1
    nd = 0
    while(n<numero):
        if(numero%n==0):
            nd = nd+1
        else:
            pass
        n += 1
    return nd