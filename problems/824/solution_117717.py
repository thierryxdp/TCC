def uppCons(frase):
    """ Funçao que retorna uma frase com todoas as suas consoantes em
    maiusculas """
    i = 0
    consoante = 'bcdfghjklmnpqrstvwxyz'
    while i <(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase:
            consoante = consoante.upper(frase[i])
            i=i+1
            return frase