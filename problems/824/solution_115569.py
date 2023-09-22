def uppCons (frase):
    """
    	Função que retorna a frase dada com suas consoantes
        maiusculas.
    	string -> string
    """
    i = 0
    maiusculas = ''
    while frase[i] in 'bcdfghjklmnpqrstvwxyz':
          maiusculas = frase[0:i]+frase[i].upper()+frase[i-1:]
        i = i + 1
    return maiusculas