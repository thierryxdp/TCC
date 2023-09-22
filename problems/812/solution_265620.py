def retira_pontuacao(frase):
    frase = re.sub("(!.,:;?/-)", " ", frase)
    return frase