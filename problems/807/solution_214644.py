def conta_frases(texto):
    '''Dado um texto armazenado em uma string, faça a funç˜ao que conte o número de frases que aparecem
neste texto'''
    #str > str
    final=0
    pont = '''!,.?'''
    for i in pont:
        final+=str.count(texto,pont)
    final-=2*str.count(texto,'...')
    return final