def conta_frases(texto):
    """..."""
    
    lista = str.replace(texto, '?', '.')
    lista = str.replace(lista, '!', '.')
    lista = str.replace(lista, '...', '.')
    lista = str.replace(lista, '.', '.')
    a = str.split(lista, '.')
    
    return (len(a) - 1)