def inverte(frase):
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    return = frase
    minuscula = str.lower(texto)
    return str.join(' ' ,str.split(minuscula,' ')[::-1]