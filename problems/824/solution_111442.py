def uppCons(frase):
    """ Recebe frase e retorna a mesma com suas consoantes maiusculas
    	str--->str"""
    l = join(l.upper() if l in 'bcdfghjklmnpqrstvwxyz'
                else letra for letra in frase)
    return l