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
    frase=str.split(frase," ")
   
    return frase