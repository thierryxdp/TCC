def retira_pontuacao(frase):
    """função que retorna a frase de entrada sem as pontuações gramaticais
    str --> str"""
    frase = frase.replace('.',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace('_',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(',',' ')
    return frase