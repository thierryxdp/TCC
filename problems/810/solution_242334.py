def inverte(frase):
    frase1=((((frase.replace('.',' ')).replace(',',' ')).replace('?',' ')).replace('!',' ')).replace('-',' ')
    frase2=frase1.split(' ')
    frase3=frase2[::-1]
    return 3