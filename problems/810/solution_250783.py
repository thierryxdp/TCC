def retira_pontuacao(fras):
    fras=str.replace(fras,"-"," ")
    fras=str.replace(fras,",","")
    fras=str.replace(fras,":","")
    fras=str.replace(fras,";","")
    fras=str.replace(fras,".","")
    fras=str.replace(fras,"!","")
    fras=str.replace(fras,"?","")
    return fras
def inverte(frase):
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    lfrase=str.split(frase," ")
    lfrase=list.reverse(lfrase)
    return lfrase