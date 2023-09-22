def inverte(frase):
    '''
    funcao que receb uma frase e retorna as mesmas palavras da inseirda, porém na ordem
    inversa da entrada, sem maiusculas e sem pontuacao
    
    str -> str
    '''

    tipo_travessao = str.replace (frase, ('-'), ' ')
    tipo_virgula = str.replace (tipo_travessao, (','), ' ')
    tipo_doispontos = str.replace (tipo_virgula, (':'), ' ')
    tipo_pontovirgula = str.replace (tipo_doispontos, (';'), ' ')
    tipo_pontofinal = str.replace (tipo_pontovirgula, ('.'), ' ')
    tipo_exclamacao = str.replace (tipo_pontofinal, ('!'), ' ')
    tipo_interrogacao = str.replace (tipo_exclamacao, ('?'), ' ')
    frase_separar = tipo_interrogacao.split()[-1::-1]
    frase_rejuntar =' '.join(frase_separar)
    return str.lower(frase_rejuntar)