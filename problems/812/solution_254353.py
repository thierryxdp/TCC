def retira_pontuaçao(frase):
    frase1 = (frase)
    
    return str(frase1.replace("?"," ").replace("..."," ").replace("!"," ").replace("."," "))