def inverte(frase):
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.lower(frase)
    frasel = str.split(frase,)
    return list.reverse(frasel)