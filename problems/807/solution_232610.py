def conta_frases(texto):
    ''' funcao que retorna o numero de frases em um texto. str >> int'''
    quantidade=0
    if '.' in texto:
        
        quantidade = quantidade + texto.count('.')
    if '!' in texto:
        quantidade = quantidade + texto.count('!')
    if '?' in texto:
        quantidade = quantidade + texto.count('?')
    if '...' in texto:
        quantidade = quantidade + texto.count('...')
    return quantidade