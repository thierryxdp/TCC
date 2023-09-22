def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [",", '.', '-']
    if pontuacao.contain(sinais) :
    	pontuacao.replace(sinais, ' ')
    return pontuacao