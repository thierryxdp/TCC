def conta_frases(texto):
    """funcao que conta o numero de frases que aparecem em um texto. Cada texto e terminado com
    um ponto final, ponto de exclamacao, ponto de interrogacao ou reticencias
    str->int"""
    lista = str.split(texto,'.')
    return len(lista)