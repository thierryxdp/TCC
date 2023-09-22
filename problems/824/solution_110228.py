def uppCons(frase):
    """   
    str,str-->str"""
    i=0
    consoante=''
    while i<len(frase):
        if frase[1] not in 'AEIOUaeiou':
            consoante= consoante+ str.upper(frase[1])
        i=i+1
    return consoante