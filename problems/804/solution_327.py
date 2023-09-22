def filtra_pares(tupla):
    """filtra os pares 
    tupla -> tupla"""
    tupla=(a,b,c,d)
    resultado=()
    if (a%2)==0:
       resultado=resultado+(a,)
    elif (b%2)==0:
       resultado=resultado+(b,)
    elif (c%2)==0:
       resultado=resultado+(c,)
    elif (d%2)==0:
       resultado=resultado+(d,)
    return resultado