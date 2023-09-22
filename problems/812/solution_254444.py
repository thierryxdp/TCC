def retira_pontuacao(frase):
    frase1 = str.join(" ",frase)  
    return frase1.replace("?"," ").replace("..."," ").replace("!"," ").replace("."," ")