def retira_pontuacao (frase):
    '''funcao que substitua as pontuacoes por espaco'''
    frase=(frase,"pontuacao")
    frase=str.replace("pontuacao",frase)
    return frase