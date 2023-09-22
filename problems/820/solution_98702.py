def posLetra(frase,l,o):
    i=0
    n=0
    if str.count(frase,l)<o:
        return -1
    else:
        while n!= str.count(frase,l):
            if frase[i]==l:
                n=n+1
                i=i+1
        return i