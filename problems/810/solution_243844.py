def inverte(s):
    ''' funcao recebe uma funcao, tira as pontuacoes da frase e 
    inverte ela de tras para frente. str-->str'''
    s = retira_pontuacao(s)
    return s[::-1]