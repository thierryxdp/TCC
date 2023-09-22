def retira_pontuacao (pontuacao):
    '''funcao que substitua as pontuacoes por espaco'''
    pontuacao.replace(pontuacao,' ')
    return len(pontuacao)