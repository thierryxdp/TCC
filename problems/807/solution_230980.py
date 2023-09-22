def conta_frases(frase):
    for c in '!':
        texto = frase.replace(c, '#')
    for c in '?':
        texto = texto.replace(c, '#')
    for c in '...':
        texto = texto.replace(c, '#')
        return len(str.split(texto, '#'))