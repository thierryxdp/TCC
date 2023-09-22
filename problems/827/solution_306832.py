def qtd_divisores(numero):
    """Funcao que retorna quantos divisores tem determinado numero
    int --> int"""
    divisores = []
    for i in range(numero):
        if numero % (i + 1) == 0:
            divisores = divisores + [i + 1]
    return len(divisores)