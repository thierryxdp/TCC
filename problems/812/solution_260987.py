def retira_pontuacao(frase):
    """dada uma frase, retorna a frase onde todos os 
    caracteres de pontuacao tenham sido substituidos
    por espaco
    str -> str"""
    x = str.replace(frase,"!"," ")
    x2 = str.replace(x,"?"," ")
    x3 = str.replace(x2,"."," ")
    x4 = str.replace(x3,"..."," ")
    x5 = str.replace(x4,","," ")
    x6 = str.replace(x5,":"," ")
    x7 = str.replace(x6,";"," ")
    x8 = str.replace(x7,"-"," ")
    return x8