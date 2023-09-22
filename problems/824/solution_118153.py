def uppCons(frase):
    '''Retorna uma frase com todas as suas consoantes em maiúsculas(e os demais
    caracteres extamente como estavam na frase original.
    frase --> str '''
    i = 0
    consoantes = 'bcdfghjklmnopqrstvwxyz'
    frase_nova= frase
    while i< len(frase):
        if frase[i] in consoantes:
            frase_nova = str.upper(frase_nova)
        return frase_nova