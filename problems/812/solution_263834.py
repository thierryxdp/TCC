def retira_pontuacao(frase):
    '''Esta funcao retorna uma frase com todos os caracteres substituidos por espaco.'''
    '''str --> str'''
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, '-', ' ')
    return frase