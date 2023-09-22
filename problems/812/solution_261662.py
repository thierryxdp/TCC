def retira_pontuacao(frase):
    '''Ao receber uma frase, substitui todas as pontuações
    por espaço
    str -> str'''
    #substituindo as pontuações por espaço
    travessao = str.replace(frase,'-',' ')
    virgula = str.replace(travessao,',',' ')
    dois_pontos = str.replace(virgula,':',' ')
    ponto_virgula = str.replace(dois_pontos,';',' ')
    exclamacao = str.replace(ponto_virgula,'!',' ')
    interrogacao = str.replace(exclamacao,'?',' ')
    ponto = str.replace(interrogacao,'.',' ')
    return ponto