def retira_pontuacao(frase):
    """
    funcao que dada uma frase pontuada, remove todos os pontos
    como travessao, virgula, dois pontos, ponto e virgula e 
    ponto final e substitui por espaço.
    :param frase: str 
    :return: str
    """
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_pontos = virgula.replace(':', ' ')
    ponto_virgula = dois_pontos.replace(';', ' ')
    ponto_final = ponto_virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    return ponto_exclamacao