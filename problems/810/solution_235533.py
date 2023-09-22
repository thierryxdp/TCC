def inverte(frase):
    frase=frase.replace('.',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.split()
    frase=list(frase)
    frase=frase[::-1]
    frase=str.join(' ',frase)
    nova_frase=str(frase)
    return nova_frase.lower()