def retira_pontuacao(frase):
    frase1 = str.join(" ",frase)  
    return change.join(frase).replace("?"," ").replace("..."," ").replace("!"," ").replace("."," ")