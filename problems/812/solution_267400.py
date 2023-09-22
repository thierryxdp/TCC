def retira_pontuacao(frase):
    caracteres = '-,:;.!?'
    for c in caracteres:
        frase = frase.replace(c, ' ')
    return frase