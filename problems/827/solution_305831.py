def qtd_divisores(n):
    """ Função que retorna a quantidade de divisores de 
    um némero.
    Entrada: int
    Saída: int """
    total = 0
    for divisor in range(1,n+1):
        if n%divisor == 0:
            total = total + 1
    return total