def inverte(frase):
    frase = frase.replace('.',' ').replace(',',' ').replace('-',' ').replace('?',' ').replace('!',' ')
    frase = frase.split()
    frase = frase[::-1]
    frase = frase.join()
    r