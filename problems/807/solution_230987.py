def conta_frases(frase):
    for c in '!':
        texto = frase.replace(c, '#')
    for c in '?':
        texto = texto.replace(c, '#')
    for c in '.':
        texto = texto.replace(c, '#')
    for c in ':':
        texto = texto.replace(c, '#')
    if str.count(texto,'.')>0:
        return 2
    return len(str.split(texto, '#'))