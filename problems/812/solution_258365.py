def retira_pontuacao(frase):
    """função que recebe uma string com uma frase e retira
    os caracteres de pontuação.
    str -> <frase>"""
    frase  = frase.replace('?',' ')
    frase  = frase.replace('!',' ')
    frase  = frase.replace(',',' ')
    frase  = frase.replace('-',' ')
    frase  = frase.replace(':',' ')
    frase  = frase.replace(';',' ')
    frase  = frase.replace('.',' ')
    
    return frase