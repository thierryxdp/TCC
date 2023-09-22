def uppCons (frase):
    '''...'''
    resposta = ()
    i=0
    consoantes = 'bcdfghjklmnpqrstuvwxyz'
    
    while i<len(frase):
        if frase[i] in consoantes:
            str.upper(frase[i])
        i+=1
    return frase