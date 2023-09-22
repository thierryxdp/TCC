def qtd_divisores(n):
    """Função que dado um número inteiro n de entrada, conta quantos divisores
    possui.
    int -> int
    """
    x = list(range(1,n+1))
    lista = []
    for numero in x:
        if n%numero == 0:
            lista += [numero]
            y = len(lista)
    return y