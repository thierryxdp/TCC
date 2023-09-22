def filtra_pares(tup):
    """Calcule e retorne os números pares de uma tupla"""
    tup = ("x","y","z","w")
    if "x" % 2 == 0:
        return "x"
    elif "y" % 2 == 0:
        return "y"
    elif "z" % 2 == 0:
        return "z"
    elif "w" % 2 == 0:
        return "w"
    else:
        return