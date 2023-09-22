def qtd_divisores(numero):
    
    ultimo=numero+1
    divisores=0
    for numero%range(1,ultimo)==0:
        divisores=divisores+numero
    return divisores