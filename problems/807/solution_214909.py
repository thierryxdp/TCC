def conta_frases(frases):
    """Esta função conta o número de frases que aparecem em um texto, onde cada frase é terminada com um ponto final, 
    de exclação, interrogação ouretircências."""
    '.' != '...'
    ponto = str.count(frases,'.',0)
    exclamacao = str.count(frases,'!',0)
    duvida = str.count(frases, '?', 0)
    reticencias = str.count(frases, '...',0)