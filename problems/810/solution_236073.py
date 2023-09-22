def inverte(frase):
    '''retira a pontuação de uma frase e a inverte
    str -> str'''
    
    frase=frase.replace(',',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('?',' ')
    
    str.lower(frase)
    return frase