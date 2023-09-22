def retira_pontuacao(frase):
    frase = .sub("(!.,:;?/-)", " ", frase)
    return frase