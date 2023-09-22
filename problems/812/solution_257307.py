def retira_pontuacao(frase):
    frase1=str.join(" ",str.split(frase,""))
    frase2=str.join(" ",str.split(frase,"-"))
    frase3=str.join(" ",str.split(frase,","))
    frase4=str.join(" ",str.split(frase,":"))
    frase5=str.join(" ",str.split(frase,";"))
    frase6=str.join(" ",str.split(frase,"."))
    return frase6