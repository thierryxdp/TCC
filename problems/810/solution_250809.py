def retira_pontuacao(frase):
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,",","")
    frase=str.replace(frase,":","")
    frase=str.replace(frase,";","")
    frase=str.replace(frase,".","")
    frase=str.replace(frase,"!","")
    frase=str.replace(frase,"?","")
    return frase
def inverte(a):
    a=str.lower(a)
    a=retira_pontuacao(a)
    a=str.split(a," ")
    list.reverse(a)
    a=str.join(" ",a)
    return a