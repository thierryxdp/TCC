def posLetra(frase,l,o):
    i=0
    n=0
    if str.count(frase,l)<o:
        return -1
    else:
        while i<len(frase):
            if frase[i]=l:
                return i