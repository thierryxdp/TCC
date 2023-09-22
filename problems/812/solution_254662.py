def retira_pontuacao (frase):
    #Função que dada uma frase retorna a frase com os caracteres de pontuação substituídos por espaço.
    #string -> string
    frase=frase.replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("-"," ")
    return frase