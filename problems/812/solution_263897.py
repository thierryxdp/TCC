def retira_pontuacao(frase):
    '''Função que retira a pontuação de uma frase e substitui
    por espaços
    valores: str --> str'''
    frase= frase.replace('.',' ')
    frase= frase.replace('!',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace(',',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    return frase