def uppCons(frase):
    """ Funçao que retorna uma frase com todoas as suas consoantes em
    maiusculas """
    i = 0
    c = ''
    while i <(len(frase)):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.join(str.upper('bcdfghjklmnpqrstvwxyz',c)
        if 'AEIOUaeiou' in [frase[i]]:
            str.join(str.lower('AEIOU',c)
            i=i+1
            return frase