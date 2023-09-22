def retira_pontuaçao(frase):
    change= " "
    return change.join(frase).replace("?"," ").replace("..."," ").replace("!"," ").replace("."," ")