def retira_pontuacao(pontuacao):
    '''funcao que retira a pontuacao da frase'''
    sinais = [",", '.', '-', ':', '!', '?']
    frase = pontuacao
    for sinal in sinais:
        frase = palavra.replace(sinal, ' ')
    return frase