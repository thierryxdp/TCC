def conta_frases(texto):
    """
    Código que conta um número de frases que aparecem em um texto
    :entrada --> string:
    :return --> int:
    """
    string2= str.replace(texto.replace('?','m'), '!', 'm')
    string3= string2.replace('...','m')
    if ('.' or '!' or '?' in texto):
        return len(string3.strip('))