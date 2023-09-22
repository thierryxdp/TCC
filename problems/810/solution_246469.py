def retira_pontuacao(frase):
    frase=frase.replace('.',' ').replace(',',' ').replace(':',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ')
    return frase

def inverte(frase):
    
    frase=str.lower(frase)
    frase=retira_pontuacao(frase)
    frase=str.split(frase)
    frase=' '.join(frase[::-1])
    return frase