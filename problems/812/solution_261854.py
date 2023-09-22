def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [",", '.']
    pontuacao.format(sinais, ' ')
    return pontuacao