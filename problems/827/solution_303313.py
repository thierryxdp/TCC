def qtd_divisores(n):
    """funcao que retorna a quantidade de divisores dado um numero inteiro n;
    int -> int"""

    lista = list(range(1,n+1))
    divisores = []

    if n < 0:
        return 0
    
    for termo in lista:

        if n % termo == 0:

            divisores.append(termo)
            qtd = len(divisores)

    return qtd