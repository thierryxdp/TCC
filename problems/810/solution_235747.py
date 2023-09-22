def inverte(frase):
  ''' Inverte uma dada frase sem pontuação e letras maiusculas'''
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.lower(frase)
    frase = str.split(frase)
    reversed(frase)
    frase = str.join(' ',frase)
    
    return frase