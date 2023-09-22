def retira_pontuacao(frase):
    '''Função que, dada uma frase no formato de string, retorna a mesma frase, porém, sem pontuação (travessão, vírgula, dois pontos, ponto e vírgula e ponto final), substituídas por espaço; str -> str.'''
    str.replace(frase, "-", "")
    str.replace(frase, ",", "")
    str.replace(frase, ":", "")
    str.replace(frase, ";", "")
    str.replace(frase, ".", "")
    return frase