def retira_pontuacao(frase):
    '''recebe uma frase e retorna a mesma com todas pontuações retiradas e substituidas por espaço
    str->str'''
    frase=frase.replace('.',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    return frase