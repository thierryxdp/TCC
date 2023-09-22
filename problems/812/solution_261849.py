def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [",", '.', '-']
    frase = ''
    for sinal in sinais:
    	frase += pontuacao.replace(sinal, ' ')
    return frase