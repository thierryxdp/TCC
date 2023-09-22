def retira_pontuacao(frase):
    caracteres = ['-', ',', ':', ';', '.', '!', '?', '...']
    if caracteres in frase:
        return frase.replace(caracteres[0:], ' ')