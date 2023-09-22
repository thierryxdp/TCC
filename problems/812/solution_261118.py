def retira_pontuacao (pontuacao):
    '''funcao que retire as pontuacoes e sejam substituidas por espaco'''
    pontuacao=(! or - or ; or : or .)
    pontuacao.replace('pontuacao',' ')
    return (pontuacao)