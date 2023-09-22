def qtd_divisores(numero):
    i=1
    valor=0
    while i<numero:
        if numero%i==0:
            valor=valor + i
            i=i+1
    return valor