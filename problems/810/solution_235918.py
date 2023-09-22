def inverte(frase):
    """ """
    
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    
    frase = frase.lower()
  
	lista = lista[::-1]
    lista = frase.split(' ')
    
    
    return ' '.join(lista)