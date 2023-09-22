def retira_pontuacao(frase):
    """Função que substitui toda a pontuação de uma frase por espaço"""
    """string->string"""
    frase1=str.replace(frase,","," ")
    frase2=str.replace(frase1,"."," ")
    frase3=str.replace(frase2,"!"," ")
    frase4=str.replace(frase3,"-"," ")
    frase5=str.replace(frase4,":"," ")
    frase6=str.replace(frase5,";"," ")
    frase7=str.replace(frase6,"?"," ")
    return frase7
def inverte(frase):
    frase1=str.split(retira_pontuacao(frase))
    list.reverse(frase1)
    return str.join(" ",frase1)