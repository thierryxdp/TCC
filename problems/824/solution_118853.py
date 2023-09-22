def uppCons(frase):
    """Função que transforma as consoantes de uma frase em
    maiúsculas.
    str -> str"""
    
    i = 0
    
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            frase = str.replace(frase,frase[i],str.upper(frase[i]))
		i += 1
    return frase