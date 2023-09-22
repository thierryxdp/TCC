def qtd_divisores(num):
    qtd_div=0
    for i in range(num):
        if num%i==0:
            qtd_div=qtd_div+1
    return qtd_div