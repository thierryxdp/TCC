def retira_pontuacao(s):
    '''funcao que ira substituir sua pontuacao, str-->str'''
    pontuacao = "-,:;.,?!"
    for p in pontuacao:
    s = s.replace(p,"")
    return s