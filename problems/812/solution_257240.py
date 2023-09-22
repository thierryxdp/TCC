#defini frase como parametro e chamei strings com nomes dos pontos para pode removelos das frases
def retira_pontuacao(frase):
    """Dada uma frase pontuada, remove todos os pontos como travessao, virgula, dois pontos,
    e ponto final substituindo por espaço,
     str -> str"""
    travessao = frase.replace('_', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontointerrogacao.replace('!', ' ')
    return pontoExclamacao