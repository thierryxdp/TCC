frase=frase.replace('.',' ')
frase=frase.replace(',',' ')
frase=frase.replace(':',' ')
frase=frase.replace('?',' ')
frase=frase.replace('-',' ')
frase=frase.replace('_',' ')
return frase

def inverte(frase):
    frase=retira_pontuacao(frase)
    frase=str.split(frase,)
    frase=list(frase[::-1])
    frase=str.join(' ',frase)
    frase=str.lower(frase)
    return frase