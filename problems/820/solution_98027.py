def posLetra(palavra,letra,num):
    """ """
    i=0
    vezes=[]
    while i<len(palavra):
        if palavra[i]==letra:
            vezes=vezes+ [i]
        i=i+1
    return vezes