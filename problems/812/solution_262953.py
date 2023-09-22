def retira_pontuacao(frase):
    pontos = ".,:;-?"
    for v in frase:
        if v in pontos:
            frase = frase.replace(v, ' ')
    return frase