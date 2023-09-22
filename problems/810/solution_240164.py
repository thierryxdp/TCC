def inverte(frase):
   
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
 
    minuscula = str.lower(frase)
    return str.join(' ',str.split(minuscula,'')
    [::-1])