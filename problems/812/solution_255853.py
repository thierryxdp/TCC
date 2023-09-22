def retira_pontuacao(frase):
    """retorna uma frase sem os sinais de pontuação.str-.str"""
    frase=str.replace(frase,"..."," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,";"," ")
    return frase