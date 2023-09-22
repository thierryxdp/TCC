def retira_pontuacao(frase):
    x = frase.replace("."," ")
    x = x.replace(","," ")
    x = x.replace(";"," ")
    x = x.replace(":"," ")
    x = x.replace("-"," ")
    x = x.replace("?"," ")
    x = x.replace("!"," ")
    return x