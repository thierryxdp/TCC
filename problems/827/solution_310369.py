def qtd_divisores(n):
    c=0
    for e in range(n):
        if n%(e+1)==0:
            c+=1
    return c