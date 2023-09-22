def conta_frases(texto):
    """função que conta o numero de frases que aparecem em um texto.
    str->int"""
    ponto final=str.split(texto, '.')
    ponto inter=str.split(ponto final, '?')
    ponto ex=str.split(ponto inter,'!')
    
    frases= len(ponto ex)
    
    return frases