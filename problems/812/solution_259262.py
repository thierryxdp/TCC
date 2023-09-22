def retira_pontuacao(frase):
    map(str.replace, frase, ["...", ".", "?", "!", ",", "-"], " ")