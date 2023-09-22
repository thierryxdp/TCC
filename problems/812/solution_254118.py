def retira_pontuacao(frase):
    """Função que dada uma frase retira todos os caracteres de pontuação e os substitui por espaço
    str -> str"""
    travessao = str.replace(frase, '-', ' ')
    virgula = str.replace(travessao, ',', ' ')
    doispontos = str.replace(virgula, ':', ' ')
    pontovirgula = str.replace(doispontos, ';', ' ')
    ponto = str.replace(pontovirgula, '.', ' ')
    exclamacao = str.replace(ponto, '!', ' ')
    interrogacao = str.replace(exclamacao, '?', ' ')
    return interrogacao