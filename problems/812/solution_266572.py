def retira_pontuacao(frase):
    """dada uma frase, retorne a frase onde todos os caracteres de pontuacao (incluindo travessao, vırgula, dois pontos, ponto e vırgula, alem da pontuacao de encerramento de frase) tenham sido substituıdos por espaço"""
    frase=list.replace(frase,"-"," ")
    frase=list.replace(frase,","," ")
    frase=list.replace(frase,"."," ")
    frase=list.replace(frase,":"," ")
    frase=list.replace(frase,";"," ")
    frase=list.replace(frase,"?"," ")
    frase=list.replace(frase,"!"," ")
    return frase