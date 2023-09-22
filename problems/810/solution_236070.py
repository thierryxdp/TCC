def inverte(frase):
    '''retira a pontuação de uma frase e a inverte
    str -> str'''
    
    frase=frase.replace(',',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('?',' ')
    
    str.split(frase)
    str.join(-1,frase)
    
    return frase