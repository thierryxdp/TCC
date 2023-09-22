def inverte(frase):
    frase=frase[::-1]
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"..."," ")
    frase=str.replace(frase,"."," ")
    frase=str.lower(frase)
    frase=str.split(frase," ")
    frase=str.join(" ",frase)
    return frase