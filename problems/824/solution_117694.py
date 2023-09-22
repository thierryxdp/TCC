def uppCons(frase):
    """ Funçao que retorna uma frase com todoas as suas consoantes em
    maiusculas """
    i = 0
    while i <(len(frase)):
        consoante = 'bcdfghjklmnpqrstvwxyz'
        consoante = consoante.upper()
        vogais = 'AEIOU'
        vogais = vogais.lower()
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
            str.upper(frase[i])
            i = i+ 1
        if frase[i] in 'AEIOU':
            str.lower(frase[i])
            i=i+1
            return frase