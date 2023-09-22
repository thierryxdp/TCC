def retira_pontuacao(frase):
	'''
    funcao que rece uma frase e retorna a mesma 
    trocando toda a pontuação por espaço
    
    str -> str
    '''
    
    tipo_travessao = str.replace (frase, ('-'), ' ')
    tipo_virgula = str.replace (tipo_travessao, (','), ' ')
    tipo_doispontos = str.replace (tipo_virgula, (':'), ' ')
    tipo_pontovirgula = str.replace (tipo_doispontos, (';'), ' ')
    tipo_pontofinal = str.replace (tipo_pontovirgula, ('.'), ' ')
    tipo_exclamacao = str.replace (tipo_pontofinal, ('!'), ' ')
    tipo_interrogacao = str.replace (tipo_exclamacao, ('?'), ' ')
    return tipo_interrogacao