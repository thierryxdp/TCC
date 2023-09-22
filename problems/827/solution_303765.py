def qtd_divisores(n):
    div=0
    for i in range(1, int(n/2+1)):
        if n % i == 0: 
            div=div+n[i]
    return div