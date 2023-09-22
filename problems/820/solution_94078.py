def posLetra(string, achar, start):
    """ Encontre e retorne o índice de achar em string.
      Retorne -1 se achar não ocorrer em string.
    """
    ix = start
    found = False
    while ix < len(string) and not found:
        if string[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1