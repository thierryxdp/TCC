def conta_frases(frase):
    '''
    Conta o número de frases em um texto, considerando que uma frase termina
    com ..., !, ? ou .
    
    string -> int
    '''
    if "..." in frase:
        pontos = frase.count(".") - 2*frase.count("...")
    else:
        pontos = frase.count(".")
    return frase.count("!") + frase.count("?") + pontos