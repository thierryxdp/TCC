def retira_pontuacao(fras):
    fras=str.replace(fras,"-"," ")
    fras=str.replace(fras,","," ")
    fras=str.replace(fras,":"," ")
    fras=str.replace(fras,";"," ")
    fras=str.replace(fras,"."," ")
    fras=str.replace(fras,"!"," ")
    fras=str.replace(fras,"?"," ")
    return fras
def inverte(frase):
    frase=retira_pontuacao(frase)
    return frase