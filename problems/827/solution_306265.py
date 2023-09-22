def qtd_divisores(n):
    cont=0
    for iee in range(1,n+1):
        if n%iee==0:
            cont+=1
    return cont