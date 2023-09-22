def conta_frases(texto):
    '''
    '''
    texto=texto.replace('?','!','.','...')
   
    return len(texto.split())