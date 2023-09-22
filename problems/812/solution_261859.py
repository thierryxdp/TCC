def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [",", '.']
    for sinal in sinais:
    	pontuacao.replace(sinais[sinal], ' ')
    return pontuacao