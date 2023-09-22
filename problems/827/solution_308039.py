def qtd_divisores(x):
    divisores=()
    for i in range(1, int(num/2+1)):
        if num%i==0:
            divisores=divisores+num
    return sum(num)