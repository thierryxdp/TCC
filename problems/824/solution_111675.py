def uppCons (frase):
    '''...'''
    resposta = ()
    i=0
    contadorcons = 0
    consoantes = 'bcdfghjklmnpqrstuvwxyz'
    
    while i<len(frase):
        if frase in str.upper(consoantes):
            contadorcons += 1
        i+=1
    return contadorcons