def conta_frases(frase):
    """Essa Função dada um texto, ela retorna o numero de frases desse texto;
    Recebe um texto;
    Retorna o numero de palavras nesse texto.
    string -> int"""
    f = frase.split('!')
    frase = '.'.join(f)
    f = frase.split('?')
    frase = '.'.join(f)
    f = frase.split('...')
    frase = '.'.join(f)
    f = frase.split('.')
    return len(f)