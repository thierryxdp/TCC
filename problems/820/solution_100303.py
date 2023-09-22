def posLetra(astring, achar, start=0, end=None):
        """
          Find and return the index of achar in astring.
          Return -1 if achar does not occur in astring.
        """
        i = start
        if end == None:
           end = len(astring)

        found = False
        while i < end and not found:
            if astring[i] == achar:
                found = True
            else:
                i=+ 1
        if found:
            return i
        else:
            return -1