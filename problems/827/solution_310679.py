def qtd_divisores(x):
    divisores = ()
    for num in range(1,x+1):
        if x%num == 0:
            divisores = divisores + (num ,)
    return divisores