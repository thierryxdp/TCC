def inverte(frase):
    """ """
    
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'-',' ')
    
    frase = str.lower(frase)
  
    lista = str.split(frase,' ')
    
    return str.join(' ',lista[:-1])