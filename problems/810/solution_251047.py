def retira(frase):
    frase1=str.replace(frase,"."," ")
    frase2=str.replace(frase1,","," ")
    frase3=str.replace(frase2,"?"," ")
    frase4=str.replace(frase3,":"," ")
    frase5=str.replace(frase4,";"," ")
    frase6=str.replace(frase5,"!"," ")
    frase7=str.replace(frase6,"-"," ")
    return frase7
def inverte(frase7):
    frase8=str.lower(frase7)
    
    return frase8