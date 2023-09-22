def retira_pontuacao (frase, pontuacao):
    '''funcao que substitua as pontuacoes por espaco'''
    lista =str.pontuacao
    for pontuacao in lista:
    frase.replace(pontuacao," ")
    return frase