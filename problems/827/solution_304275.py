def qtd_divisores(n):
    divisores = 0
    for numero in range(1,n+1):
        if n%numero == 0:
            divisores += 1
        else:
            pass
    return divisores
    
divisores(10)