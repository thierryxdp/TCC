def qtd_divisores(n):
    """Funcao que calcula o numero de divisores.Int-->List"""
    lista = range (1,n+1)
    qtd_divisores = 0
    for count in lista:
        if n % count == 0:
            qtd_divisores = qtd_divisores + 1
    return qtd_divisores