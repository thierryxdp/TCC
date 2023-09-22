def qtd_divisores(x):
    divisores=()
    for i in range(x):
        if x%i==0:
            divisores=divisores+x
    return sum(x)