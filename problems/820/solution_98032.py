def posLetra(palavra,letra,num):
    """ """
    i=0
    vezes=[]
    while i<len(palavra):
        if palavra[i]==letra:
            vezes=vezes+ [i]
        i=i+1
    if num> len(vezes):
            return -1
    else: return vezes[num-1]