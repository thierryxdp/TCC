def qtd_divisores(numero):
    divisores=0
    for poss_divi in range(1,numero+1):
        if numero%poss_divi==0:
            divisores+=1
    return divisores