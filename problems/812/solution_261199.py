def retira_pontuacao(frase):
    """ Dada uma frase, retorna a mesma frase onde as pontuações de travessão, vírgula, dois pontos, ponto e vírgula, ponto, exclamação, interrogação 
    são substituídas por espaço
    str -> str """
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')