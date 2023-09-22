def posLetra(palavra,letra,num):
    """ """
    i=0
    vezes=[]
    while i<len(palavra):
        if palavra[i]==letra:
            vezes=vezes+ [i]
        i=i+1
    if len(vezes) <= num:
        return vezes[num-1]
    else: return -1