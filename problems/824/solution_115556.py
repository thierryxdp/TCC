def uppCons (frase):
    """
    	Função que retorna a frase dada com suas consoantes
        maiusculas.
    	string -> string
    """
    i = 0
    maiusculas = ''
    while frase[i] in 'AEIOUbcdfghjklmnpqrstvwxyz':
          maiusculas += frase[1].upper()
    i = 0 + 1
    return maiusculas