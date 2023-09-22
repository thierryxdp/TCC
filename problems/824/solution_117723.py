def uppCons(frase):
    """ Funçao que retorna uma frase com todas as suas consoantes em maiusculo """
    i = 0
    consoante = 'bcdfghjklmnpqrstvwxyz'
    while i <(len(frase)):
        if consoante in frase[i]:
            consoante.upper(frase[i])
            i=i+1
        return frase