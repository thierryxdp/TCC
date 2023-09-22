def lingua_p(palavra):
    
    P = str.upper(palavra)
    i=0
    idioma = ''
    while i < len(P):
        if P[i] not in 'BCDFGHJKLMNPQRSTVWXYZÇ':
        
        	idioma += P[i]+'P'+P[i]
        else:
            idioma += P[i]
		i+=1
        
    diminuir = str.lower(idioma)
	
    return diminuir