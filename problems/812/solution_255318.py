def retira_pontuacao (frase):
    '''Funcao que, dada uma frase, retorna a frase onde todos os caracteres de pontuacao sao substituidos por espaco'''
    '''str -> str'''

    ponto = frase.replace ('.',' ')
    virgula = ponto.replace (',',' ')
    exclamacao = virgula.replace ('!',' ')
    interrogacao = exclamacao.replace ('?',' ')
    dois_pontos = interrogacao.replace (':',' ')
    ponto_virgula = dois_pontos.replace (';',' ')
    travessao = ponto_virgula.replace('-',' ')
    return travessao