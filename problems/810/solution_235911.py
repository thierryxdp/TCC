def inverte(frase):
    """ """
    
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'-',' ')
    
    frase = str.lower(frase)
  
    lista = frase.split(' ')
    lista = lista[::-1]
    
    return ' '.join(lista)