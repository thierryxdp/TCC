def retira_pontuacao(frase):
    """função que dada uma frase,retorne a frase com os caracteres de pontuação substituidos por espaços"""
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    return str.replace(frase,"?"," ")