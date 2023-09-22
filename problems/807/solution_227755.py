def conta_frases(texto):
    if '.' in frase0:
        frase0 = str.replace(frase0,'.',' ')
    if '!' in frase0:
        frase0 = str.replace(frase0,'!',' ')
    if '?' in frase0:
        frase0 = str.replace(frase0,'?',' ')
    if '...' in frase0:
        frase0 = str.replace(frase0,'...',' ')
    return str.count(texto,' ')