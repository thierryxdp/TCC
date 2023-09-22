def posLetra(frase, letra, num=0):
    """
      Find and return the index of achar in astring.
      Return -1 if achar does not occur in astring.
    """
    i=0
    ix = num
    tem = False
    while i < len(frase) and not tem:
        if frase[i] == letra:
            tem = True
        else:
            ix = ix + 1
    i=+1
    if tem and num<=len(letra):
        return ix
    elif num<=len(letra):
        return ix
    else:
        return -1