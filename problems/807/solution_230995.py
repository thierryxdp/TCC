def conta_frases(frase):
    for c in '!':
        texto = frase.replace(c, '#')
    for c in '?':
        texto = texto.replace(c, '#')
    for c in ':':
        texto = texto.replace(c, '#')
    if texto.count('.')>0:
        return len(str.split(texto, '#'))+texto.count('.')/2
    else:
        return len(str.split(texto, '#'))