def conta_frases(texto):
    """Dado um texto, a função realiza a contagem de cada frase.
    str->str"""
    
    lista = str.replace(texto, '?', '.')
    lista = str.replace(lista, '!', '.')
    lista = str.replace(lista, '...', '.')
    lista = str.replace(lista, '.', '.')
    a = str.split(lista, '.')
    
    return (len(a) - 1)