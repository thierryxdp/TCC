def conta_frases(frase):
    """Função que, dado um texto, conta o número de frases que aparecem nesse texto
    str -> int"""
    lista = str.split(frase, '!', '?')
    return len(lista)