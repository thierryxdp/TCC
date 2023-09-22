def qtd_divisores(n):
    'dado um numero retorne a quantidade de divisores que esse numero possui. int-->int'
    quantidade=0
    for i in range(1,n+1):
        if i%n==0:
            quantidade=quantidade+1
    return quantidade