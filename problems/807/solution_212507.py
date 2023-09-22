def conta_frases (texto):
    '''Função conta quantas frases há no texto.;
    Necessário terminar o texto com pontos (finais, exclamação, interrogação, reticências.)
    str -> int'''
    ponto = str.count (texto, '.')
    exclamacao = str.count (texto, '!')
    interrogacao = str.count (texto, '?')
    reticencias = str.count (texto, '...')
    if reticencias > 0:
        ponto = ponto - 3 * reticencias
    return ponto + exclamacao + interrogacao + reticencias