def inverte (frase, pontuacao):
    '''funcao que inverte a frase'''
    sinais = pontuacao
    frase = pontuacao 
    for sinal in sinais:
        frase = frase.replace(sinal, ' ')
    return frase 
    frase = frase.lower(frase)
    return frase