def retira_pontucao(frase):
    palavra=str.replace(frase,"!"," ")
    palavra=str.replace(frase,"?"," ")
    palavra=str.replace(frase,","," ")
    palavra=str.replace(frase,"."," ")
    return palavra