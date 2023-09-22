def uppCons(frase):
    
    i = 0
    consoantes = 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm'
    frase2 = ''
    
    while i<len(frase):
        if frase[i] in consoantes:
            str.upper(frase[i])
    return frase