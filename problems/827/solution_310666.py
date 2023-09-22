def qtd_divisores(num):
    divisores=0
    divisor=1
    while divisor<=num:
        if num%divisor==0:
            divisores+=1
    return divisores