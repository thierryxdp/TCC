def retira_pontuacao(frase):
    '''Retorna a frase onde todos os caracteres de pontuação tenham sido
    substituídos por espaço.
    frase->str '''
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(',',' ')
    return frase