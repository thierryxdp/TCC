def retira_pontuaçao(frase):
    '''Retorna uma frase onde todos os caracteres de pontuação são
    substituidos por espaço'''
    
    frase = frase.replace('!', ' ')
    frase = frase.replace ('...', ' ')
    frase = frase.replace ('.', ' ')
    frase = frase.replace ('?', ' ')
    frase = frase.replace ('_', ' ')
    frase = frase.replace (':', ' ')
    frase = frase.replace ('-', ' ')
    frase = frase.replace (',', ' ')
    return frase