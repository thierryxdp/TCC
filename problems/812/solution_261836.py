def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = ',''.'
    frase = pontuacao.replace(sinais, ' ')
    return frase