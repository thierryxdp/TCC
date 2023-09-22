def qtd_divisores (n):
    d = ()
    for i in range(n):
        if i%n == 0: 
            d+i
    return d