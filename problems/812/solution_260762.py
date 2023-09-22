def retira_pontuacao (frase,pontuacao):
    '''funcao que substitua as pontuacoes por espaco'''
    return frase[0:pontuacao]+' '+frase[pontuacao+1:]