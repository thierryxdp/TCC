def inverte(frase):
    frase=frase.replace(',',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    frase= frase.split()
    frase= frase[::-1]
    return ((((','.join(frase)).replace(',',' ')).lower())).strip()