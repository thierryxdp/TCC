def qtd_divisores(num):
    divisores=0
    for divisor in range(num):
        if num%divisor==0:
            divisores=divisores+1
            
    return divisores