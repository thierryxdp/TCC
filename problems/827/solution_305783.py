def qtd_divisores(numero):
    
    div=list(range(1,ultimo))
    ultimo=numero+1
    divisores=0
    i=0
    for numero%div[i]==0:
        divisores=divisores+numero
    i=i+1
    return divisores