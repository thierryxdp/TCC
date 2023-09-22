def subistui_pontuacoes_por_espacos(s):
    ''' funcao recebe uma frase, e onde aparacer -,:;., ela ira subistituir por
espacos. str-->str'''
    pontuacao = "-,:;.,?!"
    for p in pontuacao:
        s = s.replace(p," ")
    return s