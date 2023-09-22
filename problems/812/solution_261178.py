def retira_pontuacao(frase):
    str.strip(frase, "-")
    str.strip(frase,',')
    str.strip(frase,":")
    str.strip(frase,";")
    str.strip(frase,".")
    return frase