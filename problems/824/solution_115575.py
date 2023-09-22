def uppCons (frase):
    """
    	Função que retorna a frase dada com suas consoantes
        maiusculas.
    	string -> string
    """
    i = 0
    maiusculas = ''
    while i<len(frase):
        if frase[i] in 'AEIOUbcdfghjklmnpqrstvwxyz':
            maiusculas += frase[i].upper()
        i = i+1         
        
    return maiusculas