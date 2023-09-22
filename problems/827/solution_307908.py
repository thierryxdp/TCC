def qtd_divisores(n):
    D=[]
    for N in range(1,n+1):
        if n % N == 0:
            list.append(D,N)
    return len(D)