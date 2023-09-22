def qtd_divisores(numero):
    a=0
    for i in range(1,numero+1):
        if numero%i==0:
            a+=1
    return a