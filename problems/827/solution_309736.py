def qtd_divisores(n):
    """
    funcao que conta quantos numeros divisores um numero tem
    int, int -> int
    """
    i=0
    for caractere in range(1,n+1):
        if n%caractere==0:
            i=i+1
    return i