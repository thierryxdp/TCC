def inverte(frase):
    frase1=((((frase.replace('.',' ')).replace(',',' ')).replace('?',' ')).replace('!',' ')).replace('-',' ')
    frase2=frase1[::-1]
    return frase2