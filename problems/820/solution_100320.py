def posLetra(frase, letra, n=0):
        """
          Find and return the index of achar in astring.
          Return -1 if achar does not occur in astring.
        """
ix = start
tem = False
    while ix < len(frase) and not tem:
        if frase[ix] == letra:
            tem = True
        else:
            ix = ix + 1
    if tem and len(letra)==n:
        return ix
    else:
        return -1