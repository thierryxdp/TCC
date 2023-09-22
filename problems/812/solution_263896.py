def retira_pontuacao(frase):
    '''Função que retira a pontuação de uma frase e substitui
    por espaços
    valores: str --> str'''
    frase.replace('.',' ')
    frase.replace('!',' ')
    frase.replace('?',' ')
    frase.replace(',',' ')
    frase.replace('-',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    return frase