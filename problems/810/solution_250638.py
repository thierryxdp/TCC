def retira_pontuacao(frase):
    d=[".",",","-",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase