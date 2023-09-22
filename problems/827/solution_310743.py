def qtd_divisores(x):
    n = 1
    divisores = 0
    while n != x:
        if x >0:   
            if x%n == 0:
                divisores += 1
            n += 1
    return(divisores)