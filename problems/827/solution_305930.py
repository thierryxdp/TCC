def qtd_divisores(n):
    divisores=[]
    i=0
    soma=range(1,n+1)
    while i<n:
        if n%soma[i]==0:
            i=i+soma[i]
    divisores=divisores+soma[i]
    return divisores