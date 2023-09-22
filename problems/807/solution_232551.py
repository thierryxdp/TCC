def conta_frases(texto):
    ''' Função que  conta as frases a partir dos separadores
    str-> int'''

    if '...' in texto:
        texto = str.replace(texto,'...','/')
    if '!' in texto:
        texto = str.replace(texto,'!','/')
    if '?' in texto:
        texto = str.replace(texto,'?','/')
    if '.' in texto:
        texto = str.replace(texto,'.','/')
    return str.count(texto,'/')