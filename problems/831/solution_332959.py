def lingua_p(palavra):
    """Função que receba uma palavra e retorne uma palavra traduzida ao português; str=>str"""
    m = palavra.lower()
    np = ''
    vogais = 'aeiouãáéíóú'
    for p in m:
        np += 'p'
        if p in vogais:
            np += 'p'
    return np