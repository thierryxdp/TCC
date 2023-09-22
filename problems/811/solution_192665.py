""" Retorna True se o colchão passa pela porta e False se não.
List[int, int, int], int, int --> string."""
def colchao(medidas,H,L):
    if medidas[1] <= H:
        return True
    elif medidas[1] <= L:
        return True
    else:
        return False