def uppCons(frase):
    """ Funçao que retorna a frase com todas as suas 
    consoantes em maisculas"""
    i = 0
    frase = ''
    while i <(len(frase)):
        consoantes = 'bcdfghjklmnpqrstvwxyz'
        if consoantes in frase:
            frase2 = str.upper(consoantes)
            return frase2