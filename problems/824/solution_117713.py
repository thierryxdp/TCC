def uppCons(frase):
    """ Funçao que retorna uma frase com todoas as suas consoantes em
    maiusculas """
    i = 0
    while i <(len(frase)):
        consoante = 'bcdfghjklmnpqrstvwxyz'
        consoante = consoante.upper()
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
            consoante = consoante.upper(frase[i])
            i=i+1
            return frase