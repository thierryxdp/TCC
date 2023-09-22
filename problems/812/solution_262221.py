def retira_pontuacao(frase):
    '''retorna uma frase sem as pontuacoes'''
    '''str -> str'''
    
    frase=frase.replace('.',' ')
    frase=frase.replace('/',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    
    return frase