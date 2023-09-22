def qtd_divisores(numero):
    d=0
    for x in range(1, numero+1):
        if numero%x==0:
            d=d+1
            return d