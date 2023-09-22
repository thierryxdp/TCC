def retira_pontuacao (frase):
    '''Dada uma frase qualquer, retorne espaços no lugar dos
       caracteres de pontuação;
       string -> string'''
    frase = frase.replace ('-', '  ')
    frase = frase.replace (',', '  ')
    frase = frase.replace (':', '  ')
    frase = frase.replace (';', '  ')
    frase = frase.replace ('?', '  ')
    frase = frase.replace ('!', '  ')
    frase = frase.replace ('.', '  ')
    return frase