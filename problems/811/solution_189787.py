def colchao(medidas,H,L):
    """A função recebe como entradas uma lista (cujos elementos
    são ints que representam as 3 dimensões de um colchão), a altura
    e a largura de uma porta (ints) e retorna o booleano
    True, se for possível que o colchão passe pela porta, e False,
    caso não seja possível."""
    if min(medidas[1], medidas[2]) > max(H,L):
        return False
    else:
        return True