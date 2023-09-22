#3
def retira_pontuacao(texto):
    texto=replace("-"," ")
    texto=replace(","," ")
    texto=replace(":"," ")
    texto=replace(";"," ")
    texto=replace("."," ")
    texto=replace("!"," ")
    texto=replace("?"," ")
    return texto