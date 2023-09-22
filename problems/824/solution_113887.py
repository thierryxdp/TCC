def uppCons(frase):
    
    i = 0
    consoantes = 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm'
    frase2 = ''
    
    while i<len(frase):
        if i in consoantes:
            frase2 = i.upper()
    return frase2