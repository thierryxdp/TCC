def qtd_divisores(n):
    """Quantos divisores possui um número n
       int ~> str"""
    soma = 0 
    for num in range(0,n+1):
        if n%num == 0:
            soma+= 1
    return soma