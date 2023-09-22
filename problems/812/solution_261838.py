def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [',', '.']
    for x in sinais:
        frase = pontuacao.replace(sinais, ' ')
    return frase