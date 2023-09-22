def retira_pontuacao(frase):
    change= " "
    return change.join(frase).replace("?"," ").replace("..."," ").replace("!"," ").replace("."," ")