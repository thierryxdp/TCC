def uppCons(frase):
    '''Retorna uma frase com todas as suas consoantes em maiúsculas(e os demais
    caracteres extamente como estavam na frase original.
    frase --> str '''
    i = 0
    frase_nova = frase
    while i< len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase_nova = frase_nova.replace(frase_nova[i], str.upper(frase_nova[i]))
        i= i+1
    return frase_nova