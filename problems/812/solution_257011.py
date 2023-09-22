def retira_pontuacaoo(frase):
    txt=(frase)
    if str.count(frase,".")>0:
        return txt.replace("."," ")