def retira_pontuacao(frase):
    frase= str.replace(":",",")
    frase= str.replace("-",",")
    frase= str.replace(";",",")
    frase=str.replace(".",",")
    frase= str.replace(",")
    frase="".join(frase)
    return frase