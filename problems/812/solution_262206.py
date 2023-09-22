def retira_pontuacao(frase):
    """dada a frase, retorna-a com todos os caracteres de pontuação tenham sido substituídos
por espaço.
str->str"""
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"..."," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,"-"," ")
    return frase