def retira_pontuacao(frase):
    for c in '!':
        texto = frase.replace(c, '')
    for c in '?':
        texto = texto.replace(c, '')
    for c in ':':
        texto = texto.replace(c, '')
    for c in '...':
        texto = texto.replace(c, '')
        for c in ',':
        texto = texto.replace(c, '')
        return texto