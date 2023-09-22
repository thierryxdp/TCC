def uppCons(frase):
    
    i = 0
    consoantes = ''
    
    while i<len(frase):
        if i in 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm':
            consoantes = i.upper()
    return consoantes