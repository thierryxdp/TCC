def retira_pontuacao(frase):
    texto=str.replace(frase,"."," ")
    texto=str.replace(frase,","," ")
    texto=str.replace(frase,"!"," ")
    texto=str.replace(frase,"?"," ")
    return texto