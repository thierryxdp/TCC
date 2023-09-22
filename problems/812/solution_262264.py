def retira_pontuacao (frase):
    '''substitui todos os caracteres de pontuacao por espaço'''
    '''str -> str'''
    frase = frase.replace ("."," ")
    frase = frase.replace (","," ")
    frase = frase.replace ("?"," ")
    frase = frase.replace ("!"," ")
    frase = frase.replace ("-"," ")
    frase = frase.replace (":"," ")
    frase = frase.replace (";"," ")
    return frase