def retira_pontuacao(frase):
    x = frase.replace(",", " " ) or  frase.replace("!", " " )
    return x