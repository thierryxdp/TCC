def retira_pontuacao(frase):
    ''' Função que retira a pontuação de uma determinada 
        frase e substitui por espaço.
        : param frase: str
        : return: str
    '''
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    return frase