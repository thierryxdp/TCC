def inverte(frase):
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.lower(frase)
    frase = frase.split(' ')
    list.reverse(frase)
    frase = str.join(' ',frase)
    return frase