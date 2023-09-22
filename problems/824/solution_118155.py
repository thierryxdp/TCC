def uppCons(frase):
    '''Retorna uma frase com todas as suas consoantes em maiúsculas(e os demais
    caracteres extamente como estavam na frase original.
    frase --> str '''
    i = 0
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    frase_nova= frase
    maiuscula = str.upper
    while i< len(frase):
        if frase[i] in consoantes:
            frase_nova = frase_nova + maiuscula(frase_nova)
        return frase_nova