def inverte(frase):
    '''Função que dada uma frase, retornará a mesma frase invertida
    e sem pontuação.
    tipo de entrada: str
    tipo de saída: str'''
    
    
    frase = str.replace(frase,";","")
    frase = str.replace(frase, "-"," ")
    frase = str.replace(frase, "!","")
    frase = str.replace(frase, "?","")
    frase = str.replace(frase, ",","")
    frase = str.replace(frase, ":","")
    frase = str.replace(frase, ".","")
    
    nova_frase = str.lower(frase)
    
    lista = str.split(nova_frase, ' ')
    
    nova_lista = lista[::-1]
    
    
    return str.join (" ", nova_lista)