def retira_pontuacao(frase):
    ''' Função que retorna a frase onde todos os sinais de pontuação tenham sido substituidos por espaço.
        str -> str
    '''
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,'?',' ')
    return frase