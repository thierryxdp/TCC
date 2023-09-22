def posLetra(frase, letra, num=0):
    """
      Find and return the index of achar in astring.
      Return -1 if achar does not occur in astring.
    """
    ix = num
    tem = False
    while ix < len(frase) and not tem:
        if frase[ix] == letra:
            tem = True
            ix=+1
        else:
            ix
    if tem and num==len(letra):
        return ix
    else:
        return -1