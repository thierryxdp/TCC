def retira_pontuacao(frase):
    frase1=str.replace(frase,"."," ")
    frase2=str.replace(frase1,","," ")
    frase3=str.replace(frase2,"?"," ")
    frase4=str.replace(frase3,":"," ")
    frase5=str.replace(frase4,";"," ")
    return frase5