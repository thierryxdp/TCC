def inverte(frase):
    texto = frase = str.replace(frase,'.',' ')
            frase = str.replace(frase,',',' ')
            frase = str.replace(frase,';',' ')
            frase = str.replace(frase,'!',' ')
            frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    minuscula = str.lower(texto)
    return str.join(' ' ,str.split(minuscula,' ')[::-1]