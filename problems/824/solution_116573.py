def uppCons(frase):
    """
    
    """
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            frase=str.partition(frase,frase[i])
            frase=frase[0]+str.upper(frase[1])+frase[2]
        i=i+1
    return frase