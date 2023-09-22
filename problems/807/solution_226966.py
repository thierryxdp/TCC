def conta_frases(texto):
    """
    Código que conta um número de frases que aparecem em um texto
    :entrada --> string:
    :return --> int:
    """
    string2= str.replace(texto.replace('?','.'), '!', '.')
    string3= string2.replace('...', '.')
    string4= string3.lstrip('')
    if ('.' in texto):
        return