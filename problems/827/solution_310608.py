def qtd_divisores(x):
    """Dada uma funcao que conte quantos divisores de um numero tem. 
    Entrada: int,int-->int"""
    r = 0
    for i in range(x):
        if x%(i+1) == 0:
            r = r + 1
    return r