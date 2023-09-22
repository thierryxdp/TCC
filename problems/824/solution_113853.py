def uppCons(frase):
    
    consoantes = 'qwrtopsdfghjklçzxcvbnmQWRTPSDFGHJKLÇZXCVBNM'    
    i = 0    
    
    while (i<len(frase)):
        if frase[i] in consoantes:
            consoantes = str.upper()
        i = i+1
        
    return consoantes