def qtd_divisores(numero):
    i=0
    valor=0
    while numero%i+1==0:
        valor=valor + i
        i=i+1
    return valor