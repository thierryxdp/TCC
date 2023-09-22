def conta_frases(frase):
    """Função que conta e retorna o número de frases que
    aparecem no texto dado como argumento;
    str -> int"""
    l = str.split(frase,'.') or str.split(frase,'...') or
    str.split(frase,'!') or str.split(frase,'?')
    return len(l)