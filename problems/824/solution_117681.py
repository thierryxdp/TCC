def uppCons(frase):
    """ Funçao que retorna uma frase com todoas as suas consoantes em
    maiusculas """
    i = 0
    while i <(len(frase)):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper('bcdfghjklmnpqrstvwxyz')
        if frase[i] in 'AEIOU':
            str.lower('AEIOU')
            i=i+1
            return frase