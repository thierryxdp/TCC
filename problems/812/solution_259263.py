def retira_pontuacao(frase):
    return map(str.replace, frase, ["...", ".", "?", "!", ",", "-"], " ")