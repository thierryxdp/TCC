def retira_pontuacao(frase):
    '''
       Função que recebe uma frase e a retorna sem caracteres de pontuação
       str -> str
    '''
    frase= frase.replace(',',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace('!',' ')
    return frase