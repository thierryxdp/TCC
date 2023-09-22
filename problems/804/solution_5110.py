def filtra_pares(fp):
    """Esta função que recebe uma tupla de quatro inteiros e retorna apenas os pares na mesma."""
    t = ( )
    if fp[0] %2 == 0:
             t = t +(fp[0],)
    else:
             t = t
    if fp[1] %2 == 0:
             t = t +(fp[1],)
    else:
             t = t
    if fp[2] %2 == 0:
             t = t +(fp[2],)
    else:
             t = t
    if fp[3] %2 == 0:
             t = t +(fp[3],)
    else:
             t = t
    return t