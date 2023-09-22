def qtd_divisores(numero):
    a=0
    for divisor in range(numero):
        if numero%divisor==0:
            a=a+1
    return a