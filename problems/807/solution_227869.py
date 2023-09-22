def conta_frases(texto):
    if '?' in texto:
        return len(texto.split('?'))
    elif '.' in texto:
        return len(texto.split('.'))
    elif '...' in texto:
        return len(texto.split('...'))
    elif '!' in texto:
        return len(texto.split(!))
    else :
        return ''