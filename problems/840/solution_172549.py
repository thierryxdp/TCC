def bolos(a,b,c):
    """Determinar quantos bolos dará para fazer com a quantidade disponível de trigo, ovo e leite;
    int, int, int -> int"""
    quantidade_trigo = a // 2
    quantidade_ovo = b // 3
    quantidade_leite = c // 5
    if quantidade_trigo <= quantidade_ovo and quantidade_trigo <= quantidade_leite:
        return quantidade_trigo
    elif quantidade_ovo <= quantidade_trigo and quantidade_ovo <= quantidade_leite:
        return quantidade_ovo
    else:
        return quantidade_leite