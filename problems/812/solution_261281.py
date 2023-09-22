def retira_pontuacao(frase):
    frase_nova = frase.replace("-"," ").replace(","," ").replace(":"," ").replace("."," ").replace(";"," ").replace("?"," ").replace("!"," ")
    return frase_nova