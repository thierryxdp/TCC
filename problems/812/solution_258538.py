def subs(frase):
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"—"," ")
    frase = str.replace(frase,","," ")
    return frase