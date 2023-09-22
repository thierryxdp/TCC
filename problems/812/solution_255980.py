def retira_pontuacao(frase):
    novafrase=str.replace(frase, "-", " ",-1),str.replace(frase, ",", " ",-1),str.replace(frase, ":", " ",-1),str.replace(frase, ";", " ",-1),str.replace(frase, ".", " ",-1)
    return novafrase