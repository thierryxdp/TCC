def inverte(frase):
    """  
    função que retorna a fase dada como parâmetro, na ordem inversa, com letras minúsculas e sem pontuação
    
    string -> string
    
    """
    
    frase = frase.replace('...',' ')
    frase = frase.replace(', ',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    
    frase = frase.lower()
  
    lista = frase.split(' ')
    lista = lista[::-1]
    
    
    return ' '.join(lista[1:])