def retira_pontuacao(texto:str)->str:
    #essa função retira a pontuação de um texto
    texto=texto.replace(","," ")
    texto=texto.replace(":"," ")
    texto=texto.replace("."," ")
    texto=texto.replace("!"," ")
    texto=texto.replace("-"," ")
    texto=texto.replace("?"," ")
    return texto