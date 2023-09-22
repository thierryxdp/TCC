def uppCons(frase):
    """
    	Deixa todas as consoantes de determinada frase em maiúsculo
    	str -> str
    """
    uppCons_frase = frase
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            uppCons_frase = uppCons_frase.replace(frase[i],str.upper(frase[i]))
		i += 1
    return uppCons_frase