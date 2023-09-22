def retira_pontuacao(frase):
    """funcao que recebe uma frase e retorna a mesma só que removendo todos os caracteres de pontuação e substituindo por espaço
	str -> str"""
    
    ponto = str.replace(frase, '.', ' ')
    virgula = str.replace(ponto, ',', ' ')
    travessao = str.replace(virgula, '-', ' ')
    doispontos = str.replace(travessao, ':', ' ')
    pontovirgula = str.replace(doispontos, ';', ' ')
    
    return pontovirgula