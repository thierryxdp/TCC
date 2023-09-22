def qtd_divisores(num):
    dividores=[]
    for divisor in range(num):
        if num%divisor==0:
            divisores=divisores+divisor
            
    return divisores