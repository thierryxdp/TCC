def fatorial(n):
    "Funcao calcula o fatorial de n "

    if n == 0:
        return 1
    
    resultado = n

    while n != 1:
        resultado *= (n-1)
        n -= 1

    return resultado