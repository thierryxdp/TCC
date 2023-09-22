def uppCons (frase):
    '''...'''
    resposta = ()
    consoantes = 'bcdfghjklmnpqrstuvwxyz'
    i = 0
    
    while i<len(frase):
        if frase[i] in consoantes:
            list.append(resposta,str.upper(frase[i]))
        i+=1
    return resposta