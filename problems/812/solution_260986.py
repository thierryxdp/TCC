def retira_pontuacao(frase):
    """dada uma frase, retorna a frase onde todos os 
    caracteres de pontuacao tenham sido substituidos
    por espaco
    str -> str"""
    x = str.replace(frase,"!"," ")
    x += str.replace(frase,"?"," ")
    x += str.replace(frase,"."," ")
    x += str.replace(frase,"..."," ")
    x += str.replace(frase,","," ")
    x += str.replace(frase,":"," ")
    x += str.replace(frase,";"," ")
    x += str.replace(frase,"-"," ")
    return x