def conta_frases(texto):
    """funcao que dado um texto de entrada, retorna o seu
    numero de frases;
    str -> int"""
    
    str.count(texto,'!') = exclamacao 
    str.count(texto,'?') = interrogacao
    str.count(texto,'...') = reticencias
    str.count(texto,'.') = ponto_final
    
    return exclamcao + interrogacao + reticencias + ponto_final - (3 * reticencias)