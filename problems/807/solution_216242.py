def conta_frases(frase):
    """Função que ao receber um texto, retorna o número de frases contidas nesses texto,
    baseado na pontuação;
    str -> int"""
    p = str.count(frase,'.')
    e = str.count(frase, '!')
    i = str.count(frase,'?')
    r = str.count(frase,'...')
    return p-3*r + e + i + r