def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [",", '.']
    sinall = 0
    for sinal in sinais:
    	pontuacao.replace(sinais[sinall], ' ')
        sinall++
    return pontuacao