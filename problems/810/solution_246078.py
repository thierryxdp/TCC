def inverte(frase):
    frase = str.lower(frase)
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,',',' ')
    frase = str.split(frase,' ')
    return frase