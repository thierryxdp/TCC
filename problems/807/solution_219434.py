def conta_frases(texto):
    ''' 
    string->int'''
    lista=texto.split('?' '!' '.' '...')
    return len(lista)