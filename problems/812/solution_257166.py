def retira_pontuacao(frase):
    """dada uma frase remove toda pontuação e substitui por espaço
    str -> str"""
    str(frase)
    travessao = frase.replace('_', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replac('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontointerrogacao.replace('!', ' ')
    return pontoExclamacao