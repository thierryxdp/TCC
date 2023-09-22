def retira_pontuacao(frase):
    """ retorna uma frase onde todos os caracteres de pontuacao sejam substituidos por espaco"""
    frase = str.replace (frase, '-', ' ')
    frase = str.replace (frase, ',' ,' ')
    frase = str.replace (frase, ':', ' ')
    frase = str.replace (frase, ';', ' ')
    frase = str.replace (frase, '.', ' ')
    frase = str.replace (frase, '!', ' ')
    frase = str.replace (frase, '?', ' ')
    frase = str.replace (frase, '...', ' ')
    return frase