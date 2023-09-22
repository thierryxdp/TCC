def uppCons(frase):
    """ Funçao que retorna uma frase com todoas as suas consoantes em
    maiusculas """
    i = 0
    frase = str
    while i <(len(frase)):
        consoante = 'bcdfghjklmnpqrstvwxyz'
        consoante = consoante.upper()
        vogais = 'AEIOU'
        vogais = vogais.lower()
        if consoante in frase[i]:
            str.upper(frase[i])
            i = i+ 1
        if frase[i] in vogais:
            str.lower(frase[i])
            i=i+1
            return frase