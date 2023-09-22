def retira_pontuaçao(frase):
    frase1 = str.join(" ",frase)  
    return frase1.replace("?"," ").replace("..."," ").replace("!"," ").replace("."," ")