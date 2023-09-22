def qtd_divisores(numero):
    a=1
    for divisor in range(1,numero):
        if numero%divisor==0:
            a=a+1
    return a