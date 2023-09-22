def inverte(s):
    ''' funcao recebe uma funcao, tira as pontuacoes da frase e 
    inverte ela de tras para frente. str-->str'''
    pontuacao = "-,:;.,?!"
    for p in pontuacao:
        s = s.replace(p," ")
        return s[::-1]