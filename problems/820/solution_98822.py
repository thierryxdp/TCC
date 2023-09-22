def posLetra(palavra,l,i):
    i=0
    il=0
    while i<len(palavra):
        if palavra[i]==l:
            il=il+1
            i=i+1
        return il