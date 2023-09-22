def inverte(frase):
    """ """
    
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'-',' ')
    
    frase = str.lower(frase)
  
    lista = ' '.split(frase)
    lista = lista[::-1]
    
    return ' '.join(lista)