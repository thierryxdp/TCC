def qtd_divisores(num):
    dividores=[]
    for divisor in range(num+1):
        if num%divisor==0:
            divisores=divisores+divisor
            
    return divisores