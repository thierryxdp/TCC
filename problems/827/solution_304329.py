def qtd_divisores(n):
    """Conta quantos divisores um número tem.
       int -> int"""
    
    contador = 0
    
    for i in range(1,n+1):
        if n % i == 0:
            contador += 1
    return contador