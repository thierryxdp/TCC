def inverte (frase, pontuacao):
    '''funcao que inverte frase e tira a letra maiuscula'''
    sinais= [",", '.', '-', ':', '!', '?']
    frase = pontuacao
    for sinal in sinais:
        frase= frase.replace(sinal, ' ')
        frase.reverse(frase)
        return frase