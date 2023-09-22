def inverte(frase):
    frase= str.replace(frase,'-',' ')
    frase= str.replace(frase,',',' ')
    frase= str.replace(frase,':',' ')
    frase= str.replace(frase,';',' ')
    frase= str.replace(frase,'.',' ')
    frase= str.replace(frase,'?',' ')
    frase= str.replace(frase,'!',' ')
    frase= str.lower(frase)
    frase= str.reversed(frase)
    return frase