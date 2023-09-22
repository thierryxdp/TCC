def conta_frases(texto):
    """
    dado uma string contendo um texto, retorna seu número de frases.
    """
    x=texto
    
    if '!' in x:
        x= str.replace(x,'!','.')
    if '?' in x:
        x= str.replace(x,'?','.')
    if '...' in x:
        x= str.replace(x,'...','.')
    if x[-1]=='.':
        x=x+' '
    z=str.split(x,'. ')
    return len(z)