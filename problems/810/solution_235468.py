def inverte(frase):
    
    frase = frase.replace('.',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace('?',' ')
    frase = frase.split()
    frase = frase[-1::-1]
    frase = str.join(' ', frase)
    frase = frase.lower()
    
    return frase