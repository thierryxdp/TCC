def uppCons(frase):
    
    i = 0
    consoantes = 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm'
    frase2 = ''
    
    while i<len(frase):
        if frase[i] in consoantes:
            frase2 = str.upper(frase)
    return frase2