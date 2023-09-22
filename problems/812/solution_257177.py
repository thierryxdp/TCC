def retira_pontuacao(frase):
    """dada uma frase pontuada, remove todos os pontos como, travessao. virgula, dois pontos
    e ponto final substituindo por espaço."""
    travessao = frase.replace('_', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replac('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontointerrogacao.replace('!', ' ')
    return pontoExclamacao