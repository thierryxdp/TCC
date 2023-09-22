def inverte(frase):
   
    frase1 = str.replace(frase,'.',' ')
    frase1 = str.replace(frase,',',' ')
    frase1 = str.replace(frase,';',' ')
    frase1 = str.replace(frase,'!',' ')
    frase1 = str.replace(frase,'?',' ')
    frase1 = str.replace(frase,'-',' ')
    frase1 = frase
    minuscula = str.lower(frase)
    return str.join(' ' ,str.split(minuscula,' ')
    [::-1]