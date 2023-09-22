def conta_frases(texto):
    """funcao que conta o numero de frases que aparecem no texto dado. 
    Cada frase e terminada com um ponto final, ponto de exclamacao, ponto
    de interrogacao ou reticencias
    str->int"""
    ponto = ''
    if ponto in '...?!.':
        return len(str.split(texto,ponto))
    if ponto not in '...?!.':
        return 1