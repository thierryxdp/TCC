def conta_frases(texto):
    lista = (texto.split('.'))
    lista = (lista.split('!'))
    lista = lista.split('?')
    lista = lista.split('...')
    return len(lista)