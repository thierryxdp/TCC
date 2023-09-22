def qtd_divisores(n):
    """Função que conta quantos divisores um número n tem.
       int -> int
       
       Parâmetros:
       n: o número que será contado a quantidade de divisores.
       
       returns: A quantidade de divisores de um número n.
    """
    divisores = 0
    for numeros in range(2,n+1):
        if n%numeros == 0:
            divisores += 1
    return divisores