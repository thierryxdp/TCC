def retira_pontuacao(frase):
    frase=frase.replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")
    return frase