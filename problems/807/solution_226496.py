def conta_frases(frases):
    '''Função que conta o numeo de frases que aparecem em um texto, onde cada
        frase é terminada com um ponto final, de exclação, interrogação ou
        retircências.
        Entrada: lista (str) ; Saída: int'''
    '.' != '...'
    ponto = str.count(frases,'.',0)
    exclamacao = str.count(frases,'!',0)
    duvida = str.count(frases, '?', 0)
    reticencias = str.count(frases, '...',0)
    
    return ponto + exclamacao + duvida + -2* reticencias