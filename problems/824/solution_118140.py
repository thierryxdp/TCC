def uppCons(frase):
    '''Retorna uma frase com todas as suas consoantes em maiúsculas(e os demais
    caracteres extamente como estavam na frase original.
    frase --> str '''
    i = 0
    consoantes = 'bcdfghjklmnopqrstvwxyz'
    while i< len(frase):
        if frase[i] in consoantes:
            frase = frase[i] . replace(str.upper(frase))
            i = i+1
        return frase