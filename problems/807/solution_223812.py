def conta_frases(texto):
    """..."""
    
    lista = str.replace(texto, '?', 'x')
    lista = str.replace(lista, '!', 'x')
    lista = str.replace(lista, '...', 'x')
    lista = str.replace(lista, '.', 'x')
    a = str.split(lista, 'x')
    
    return (len(a) - 1)