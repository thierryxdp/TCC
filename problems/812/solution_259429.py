def retira_pontuacao(travessao, virgula, dois pontos, ponto e virgula, ponto final):
    '''dada uma frase com os caracteres substituídos por espaço'''
    index = str.find(travessao, virgula, dois pontos, ponto e virgula, ponto final)
    size = len (frase)
    if (not index == -1) and (ponto e virgula + index + size < ponto final):
        ponto final -= index + size -1
        return travessao[:index] + retirar (travessao[index + size:], virgula, dois pontos, 0, ponto final)
    else:
        return travessao[:index] + travessao[index + size:]