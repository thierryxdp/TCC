def uppCons(frase):
    """ Funçao que retorna a frase com todas as suas 
    consoantes em maisculas"""
    i = 0
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    vogais = 'AEIOU'
    while i <(len(frase)):
        if frase[i] in consoantes:
            str.upper(consoantes)
            i = i+ 1
            return frase
        
        if frase[i] in vogais:
            str.lower(vogais)
            i=i+1
            return frase