def inverte(texto):
    ''' recebe uma frase e coloca as palavras  em ordem inversa'''
    texto = texto.replace(('-'), ' ')
    texto = texto.replace((','), ' ')
    texto = texto.replace((':'), ' ')
    texto = texto.replace((';'), ' ')
    texto = texto.replace(('.'), ' ')
    texto = texto.replace(('!'), ' ')
    texto = texto.replace(('?'), ' ')
    texto= str.lower(texto)
    texto = str.split(texto)[::-1]
    texto = str.join(' ',texto)
    return str(texto)