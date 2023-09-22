def qtd_divisores(num):
    divisores=0
    for i in list(range(1,num+1)):
        if num%i==0:
            divisores=divisores+1
    return divisores