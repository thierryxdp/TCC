def uppCons (frase):
    '''...'''
    resposta = ()
    i=0
    consoantes = 'bcdfghjklmnpqrstuvwxyz'
    palavra = str.split(frase)
        
    while i<len(frase):
        if palavra[1] in consoantes:
            list.append(resposta,str.upper(palavra))
    return resposta