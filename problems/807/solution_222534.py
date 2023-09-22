def conta_frases(texto):
    """funcao que dado um texto de entrada, retorna o seu
    numero de frases;
    str -> int"""
    
    exclamacao =  str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    ponto_final = str.count(texto,'.')
    
    return exclamcao + interrogacao + reticencias + ponto_final - (3 * reticencias)