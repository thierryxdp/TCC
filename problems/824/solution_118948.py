def uppCons(frase):
    """ Funçao que retorna uma frase com todas as suas consoantes em maiusculo """
    i = 0
    consoante = 'bcdfghjklmnpqrstvwxyz'
    while i <(len(frase)):
        if frase[i] in consoante:
            frase[i].upper()
        i=i+1
    return frase