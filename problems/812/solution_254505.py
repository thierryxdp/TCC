def retira_pontuacao(frase):
    '''retira a pontuação de uma frase
    str -> str'''
    
    frase=frase.replace(',',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('?',' ')
    return frase