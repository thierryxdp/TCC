def uppCons(frase):
    """ Funçao que retorna uma frase com todas as suas consoantes em maiusculo """
    i = 0
    while i <(len(frase)):
        consoante = 'bcdfghjklmnpqrstvwxyz'
        if consoante in frase[i]:
            consoante.upper(i)
            i=i+1
        return frase