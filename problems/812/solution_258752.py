def retira_pontuacao(frase):
    frases= frase.replaceAll("!", "").replace("?", "")
    return frases