def qtd_divisores(numero):
    divisores=1
    
    for i in range(numero):
        if numero%i == 0:
            divisores+=1

    return divisores