def filtra_pares (a, b, c, d):
    """Retorna os em formato de tupla os números pares de uma tupla de quatro números inserida.
       Entrada: tupla
       Saída: tupla
       """
    if a/2 == int(a/2):
        a = a,
    else:
        a = ""
    if b/2 == int(b/2):
        b = b,
    else:
        b = ""
    if c/2 == int(c/2):
        c = c,
    else:
        c = ""
    if d/2 == int(d/2):
        d = d
    else:
        d = ""
    return "("+a+b+c+d+")"