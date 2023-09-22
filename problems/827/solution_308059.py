def qtd_divisores(x):
    divisores=()
    for i in range(1,x):
        if x%i==0:
            divisores=divisores+(i,)     
    return divisores