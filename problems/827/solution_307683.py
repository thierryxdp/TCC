def qntd_divisores(n):
    """Dado um número n, retorna a quantidade de divisores deste n;
int -> int"""
    qntd = 0

    for divisor in range(1, n+1):
        if n%divisor == 0:
            qntd += 1
            
    return qntd