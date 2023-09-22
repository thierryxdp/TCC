def posLetra(frase, letra, start=0):
    """
      Find and return the index of achar in astring.
      Return -1 if achar does not occur in astring.
    """
    i = start
    found = False
    while i < len(frase) and not found:
        if frase[i] == letra:
            found = True
        else:
            i=+ 1
    if found:
        return i
    else:
        return -1