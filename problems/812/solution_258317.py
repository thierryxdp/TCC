retira_pontuacao (frase):
    """funcao que substitue os caracteres por espacos
    str -> str"""
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"_"," ")
    frase = str.replace(frase,","," ")
    return frase