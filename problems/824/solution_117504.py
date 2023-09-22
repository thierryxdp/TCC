def uppCons(frase):
    """ Funçao que retorna a frase com todas as suas 
    consoantes em maisculas"""
    i = 0
    while i <(len(frase)):
        consoantes = 'bcdfghjklmnpqrstvwxyz'
        if consoantes in frase:
            str.upper(consoantes)
            return frase