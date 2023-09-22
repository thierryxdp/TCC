def qtd_divisores(numero):
    i=0
    while i<numero:
        if numero%i==0:
            i=i+1
    return i