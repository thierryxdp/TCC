def conta_frases(x):
    '''funcao que conta a quantidade de frases em um texto
    str->int'''
    lista=0
    if '. ' in x:
        lista+=x.count('. ')
    if '...' in x:
        lista+=x.count('...')
    if '!' in x:
        lista+=x.count('!')
    if '?' in x:
        lista+=x.count('?')
    return lista