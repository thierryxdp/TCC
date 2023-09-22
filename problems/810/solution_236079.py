def inverte(frase):
    '''retira a pontuação de uma frase e a inverte
    str -> str'''
    
    frase=frase.replace(',',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('?',' ')
    frase=str.lower(frase)
    frase=str.split(frase)
    
    return str.join(,frase[ : :-1])