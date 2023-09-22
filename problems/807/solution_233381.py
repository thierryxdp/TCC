def conta_frases(texto):
    '''Contar frases em um texto a partir da pontuacao.
    str-->int'''
    qnt = 0
    i = 0
    frase = texto.count()
    while i <= len(frase):
        if '.' or '?' or '!' in frase[i]: 
    		qnt = qnt + 1
        i = i + 1
        return qnt