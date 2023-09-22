def inverte(frase):
   
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.lower(frase)
    frase = str.split(frase)
    frase[-4:-1]
    frase = str.join(' ',frase)
    
    return frase