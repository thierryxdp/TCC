qtd_divisores(n):
    'dado um numero, retorna a quantiade de divisores que ele possui int->int'
    k=1
    m=0
    while (k<=n):
        if (n%k==0):
            m=m+1
            k=k+1
        else:
            k=k+1
    return m