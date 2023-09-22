def uppCons(frase):
    """   
    str,str-->str"""
    i=0
    consoante=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiouãíó':
            consoante=consoante+str.upper(frase[i])
        else:
            consoante= consoante+frase[i]
        i=i+1
    return consoante