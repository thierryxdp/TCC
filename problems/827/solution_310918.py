#int->int
def qtd_divisores(num):
    divisores=0
    while divisor<=num:
        if num%divisor==0:
            divisores+=1
        divisor+=1
    return divisores