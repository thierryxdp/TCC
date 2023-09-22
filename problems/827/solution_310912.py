def qtd_divisores(num):
    while q_div<=num:
        if num%divisor==0:
            divisores+=1
        q_div+=1
    return divisores