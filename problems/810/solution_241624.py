def inverte (frase):
    '''Dada uma frase, retorne ela na ordem iversa, sem
       letras maiúsculas e sem a pontuação;
       string -> string'''
    frase = frase.replace ('-', ' ')
    frase = frase.replace (',', ' ')
    frase = frase.replace (':', ' ')
    frase = frase.replace (';', ' ')
    frase = frase.replace ('?', ' ')
    frase = frase.replace ('!', ' ')
    frase = frase.replace ('.', ' ')
    frase = str.lower (frase)
    frase = (frase [-1::-1])
    frase = "".join(frase)
    return frase