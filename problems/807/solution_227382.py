def conta_frases(texto):
    """A função recebe como entrada um texto (string) e retorna a quantidade de frases
    desse texto (int), considerando que cada frase termina com ponto final, exclamção,
    interrogação ou reticências."""
    if '...' not in texto:
        return texto.count('.') + texto.count('!') + texto.count('?')
    else:
        x = texto.count('.')
        y = texto.count('...')
        z = x - 3*y
        return texto.count('...') + texto.count('!') + texto.count('?') + z