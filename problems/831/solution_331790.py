def lingua_p(palavra):
    
    '''
    essa função tem como objetivo alterar toda a frase para maiusculo para
    identificar todas as consoantes, depois transformar elas em 'P', e por ultimo,
    transformar tudo em minusculo.
    '''
    #'str -> str -> str
    
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