def colchao(medidas, h, l):
    """
    Função que retorna True caso o colchão passe pela porta caso ao contrario retorna False;
    lista, int, int --> bool
    """
    if medidas[1] <= h or medidas[1] <= l:
        return True
    else:
        return False