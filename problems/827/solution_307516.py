def qtd_divisores(numero):
    a=0
    if numero<0:
        return 0
    for divisor in range(1,numero):
        if numero%divisor==0:
            a=a+1
    return a