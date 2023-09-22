def filtra_pares(tup):
    """Calcule e retorne os números pares de uma tupla"""
    tup = ("x","y","z","w")
    if "x" % 2 == 0:
        return "x"
    if "y" % 2 == 0:
        return "y"
    if "z" % 2 == 0:
        return "z"
    if "w" % 2 == 0:
        return "w"