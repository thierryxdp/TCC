def retira_pontuacao (frase):
    """ dada uma 'frase' de entrada, retorna esta frase onde todos os caracteres
    de pontuação (travessão, vírgula, dois pontos, ponto e vírgula, pontos de
    exclamação e interrogação) tenham sido substituídos por espaço """
    a = str.replace (frase,"!"," ")
    b = str.replace (a,"?"," ")
    c = str.replace (b,"."," ")
    d = str.replace (c,";"," ")
    e = str.replace (d,","," ")
    f = str.replace (e,"-"," ")
    g = str.replace (f,":"," ")
    return g