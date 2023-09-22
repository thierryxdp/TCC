def qtd_divisores(numero):
    
    divisores=0
    for numero%range(1,numero+1) == 0:
        divisores=divisores+numero
    return divisores