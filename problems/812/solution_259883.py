def retira_pontuacao(frase):
    frase=str.split(frase,",")
    frase1=str.join(" ",frase)
    frase2=str.split(frase1,"?")
    frase3=str.split(" ",frase2)
    return frase3