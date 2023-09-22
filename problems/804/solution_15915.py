def filtra_pares ([a, b, c, d]):
    """Retorna os em formato de tupla os números pares de uma tupla de quatro números inserida.
       Entrada: tupla
       Saída: tupla
       """
    if a/2 == int(a/2):
        e = a,
    else:
        e = ""
    if b/2 == int(b/2):
        f = b,
    else:
        f = ""
    if c/2 == int(c/2):
        g = c,
    else:
        g = ""
    if d/2 == int(d/2):
        h = d
    else:
        h = ""
    return "("+e+f+g+h+")"