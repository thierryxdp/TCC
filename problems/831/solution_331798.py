def lingua_p(palavra):
    
    Pes= str.upper(palavra)
    i= 0
    idioma = ''
    while i< len(Pes):
        if P[i] not in 'BCDFGHJKLMNPQRSTVWXYZÇ':
        
        	idioma+= Pes[i]+'P'+Pes[i]
        else:
            idioma+= Pes[i]
		i+=1
    final= str.lower(idioma)
	
    return final