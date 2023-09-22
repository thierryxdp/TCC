def conta_frases(texto):
    """Conta e retorna o número de frases que aparecem no texto de entrada.
    str->int"""
    if '...' in texto:
        return (str.count(texto,'.'))+(str.count(texto,'!'))+(str.count(texto,'?'))+(str.count(texto,'...'))-((str.count('...')*3)
                                                                                                              else:
        return (str.count(texto,'.'))+(str.count(texto,'!'))+(str.count(texto,'?'))+(str.count(texto,'...'))