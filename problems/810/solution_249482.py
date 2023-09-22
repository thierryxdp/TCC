def inverte(frase):
    frase = frase.replace('.',' ').replace(',',' ').replace('-',' ').replace('?',' ').replace('!',' ')
    for n in frase:
        inverso = frase[-n]