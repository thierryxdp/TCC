def conta_frases(texto):
    if '.' in texto:
        texto = str.replace(texto,'.','/')
    if '!' in texto:
        texto = str.replace(texto,'!','/')
    if '?' in texto:
        texto = str.replace(texto,'?','/')
    if '...' in texto:
        texto = str.replace(texto,'...','/')
    return str.count(texto,'/')