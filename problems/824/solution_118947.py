def uppCons(frase):
    """ Funçao que retorna uma frase com todas as suas consoantes em maiusculo """
    i = 0
    while i <(len(frase)):
        consoante = 'bcdfghjklmnpqrstvwxyz'
        if frase[i] in consoante:
            frase[i].upper()
            i=i+1
        return frase