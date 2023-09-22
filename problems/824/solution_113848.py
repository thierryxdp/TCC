def uppCons(frase):
    
    consoantes = ''    
    i = 0    
    
    while (i<len(frase)):
        if frase[i] in 'qwrtopsdfghjklçzxcvbnmQWRTPSDFGHJKLÇZXCVBNM':
            consoantes = str.upper(frase[i])
        i = i+1
        
    return frase