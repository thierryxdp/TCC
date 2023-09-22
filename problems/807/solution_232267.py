def conta_frases(texto):
    '''A funcao recebe um texto como entrada e retorna o numero
    de frases que estao presentes no mesmo
    str->int'''
    if '.' and '...' in texto:
        contagem= texto.count('.')-(2*texto.count('...'))
        return contagem+texto.count('?')+texto.count('!')
    else:
        return texto.count('.')+texto.count('...')+texto.count('?')+texto.count('!')