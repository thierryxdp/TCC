def uppCons (frase):
    """
    	Função que retorna a frase dada com suas consoantes
        maiusculas.
    	string -> string
    """
    i = 0
    maiusculas = ''
    while frase[i] in 'bcdfghjklmnpqrstvwxyz':
          maiusculas += frase[1].upper()
        else:
             maiusculas += frase[1]
    i = 0 + 1
    return maiusculas