def posLetra(palavra,l,p):
    i=0
    nl=0
    while i<len(palavra):
        if palavra[i]==l:
            nl=nl+1
            i=i+1
        elif nl=p:
            return i