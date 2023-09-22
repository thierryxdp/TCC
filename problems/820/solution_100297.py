def posLetra(astring, achar, start=0, end=None):
        """
          Find and return the index of achar in astring.
          Return -1 if achar does not occur in astring.
        """
        ix = start
        if end == None:
           end = len(astring)

        found = False
        while ix < end and not found:
            if astring[ix] == achar:
                found = True
            else:
                ix = ix + 1
        if found:
            return ix
        else:
            return -1