def conta_frases(texto):
    """
    Código que conta um número de frases que aparecem em um texto
    :entrada --> string:
    :return --> int:
    """
    if ('.' and '...' and '!' and '?' in texto):
        return len(texto.split('.' and '?' and '...' and '!'))