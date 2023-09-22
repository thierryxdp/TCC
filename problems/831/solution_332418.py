def lingua_p(palavra):
    P = str.upper(palavra)
    i = 0
    idioma = ''
    while i < len(P):
        if P[i] not in 'BCÇDFGHJKLMNPQRSTVWXYZ':
        	idioma += P[i]+'P'+P[i]
        else:
            idioma += P[i]
		i += 1
    return str.lower(idioma)