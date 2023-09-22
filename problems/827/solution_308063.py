def qtd_divisores(x):
    divisores=()
    for i in range(len(x)):
        if x%i==0:
            divisores=divisores+(i,)     
    return divisores