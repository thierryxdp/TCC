def retira_pontuacao (pontuacao):
    '''funcao que retire a pontuacaoo'''
    sinais = pontuacao
    frase = pontuacao 
    for sinal in sinais:
        frase = frase.replace(sinal, ' ')
    return frase 
    frase = frase.lower(frase)
    return frase