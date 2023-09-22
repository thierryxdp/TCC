def inverte(frase):
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.lower(frase)
    frase = frase.split()
    frase = frase[::-1]
    return str.join(frase)