def qtd_divisores(numero):        
    soma_divisores=0
    for a in range(1,numero+1):
        if numero%a==0:
            soma_divisores+=a
    return soma_divisores