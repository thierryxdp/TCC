def conta_frases(texto):
    ''' 
    string->int'''
    lista=texto.split('?')
    lista1=lista.split('.')
    lista2=lista1.split('...')
    lista3=[lista2.split('!')]
    return len(lista3)