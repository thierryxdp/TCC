def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [",", '.', '-']
    for sinal in sinais:
    	frase = pontuacao.replace(sinal, ' ')
    return frase