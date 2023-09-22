def qtd_divisores(n):
    """Função que conta quantos divisores um número inteiro n tem.
    int -> int """

    qtd_divisores = 0
 
    for numero in range(1, n + 1):
        if n % numero  == 0:
            qtd_divisores = qtd_divisores + 1
        

    return qtd_divisores