def inverte(frase):
    frase= frase.replace(',',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace('!',' ')
    frase=frase.lower()
    frase=frase.split()
    frase=list(frase)
    frase=frase.remove(',')
    return frase[len(frase):0:-1]