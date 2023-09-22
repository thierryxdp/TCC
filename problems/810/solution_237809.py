def retira_pontuacao(frase):
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




def inverte (frase):
    '''Dada uma frase retorna uma outra que contenha as mesmas
    palavras da frase de entrada na ordem inversa'''
    frase = retira_pontuacao(frase)
    frase = str.split(frase,)
    frase = list(frase[::-1])
    frase = str.join(' ',frase)
    frase = str.lower(frase)
    return frase