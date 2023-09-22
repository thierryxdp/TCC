def conta_frases(frase):
    '''Conta o número de frases que aparece no texto
    string -> int'''
    lista_frase = frase.split()
    frases = []
    ponto = frase.index('.')
    
    if '.' in frase:
        frases += [frase[::ponto][:]]
        del lista_frase[ponto::]
        return frases