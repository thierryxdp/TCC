def retira_pontuacao(frase):
    """
    funcao que dada uma frase pontuada, remove todos os pontos
    como travessao, virgula, dois pontos, ponto e virgula e 
    ponto final e substitui por espaço.
    :param frase: str 
    :return: str
    """
    pto_final = frase.replace('.', ' ')
    interrogacao = pto_final.replace('?', ' ')
    exclamacao = interrogacao.replace('!', ' ')
    travessao = exclamacao.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_ptos = virgula.replace(':', ' ')
    pto_virgula = dois_ptos.replace(';', ' ')
    
    return pto_virgula