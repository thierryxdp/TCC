def retira_pontuacao(frase):
    str.replace(frase, "-"," ")
    str.replace(frase,","," ")
    str.replace(frase,":"," ")
    str.replace(frase,";"," ")
    str.replace(frase,"."," ")
    return frase