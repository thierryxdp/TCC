def conta_frases(texto):
    """
    Código que conta um número de frases que aparecem em um texto
    :entrada --> string:
    :return --> int:
    """
    if ('.' or '!' or '?' in texto):
        return str.replace(texto.replace('?','.'), '!', '.') and str.split(.)