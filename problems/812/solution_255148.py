def retira_pontuacao (frase):
    """ dada uma 'frase' de entrada, retorna esta frase onde todos os caracteres
    de pontuação (travessão, vírgula, dois pontos, ponto e vírgula, pontos de
    exclamação e interrogação) tenham sido substituídos por espaço """
    str.replace (frase,"!?....:,;"," ")