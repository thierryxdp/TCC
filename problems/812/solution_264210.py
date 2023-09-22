def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da palavras'''
    sinais = [",", '.', '-', ':', '!', '?']
    palavras = pontuacao
    for sinal in sinais:
        palavras = palavra.replace(sinal, ' ')
    return palavras