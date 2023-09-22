def posLetra(frase, letra, n=0, end=None):
        """
          Find and return the index of achar in astring.
          Return -1 if achar does not occur in astring.
        """
        ix = n
        if end == None:
            end = len(frase)

        tem = False
        while ix < end and not tem:
            if frase[ix] == letra:
                tem = True
            else:
                ix = ix + 1
        if tem and len(letra)==n:
            return ix
        else:
            return -1