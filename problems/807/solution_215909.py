def conta_frases(texto):
    lista1 = (texto.split('.'))
    lista2 = (lista1.split('!'))
    lista3 = lista2.split('?')
    lista4 = lista3.split('...')
    return len(lista4)