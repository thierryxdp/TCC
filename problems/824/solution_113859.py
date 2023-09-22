def uppCons(frase):
    
    consoantes = 'qwrtopsdfghjklçzxcvbnmQWRTPSDFGHJKLÇZXCVBNM'    
    i = 0    
    
    while (i<len(frase)):
        if frase[i] in consoantes:
            frase[i] = str.upper(frase[i])
        i = i+1
        
    return frase