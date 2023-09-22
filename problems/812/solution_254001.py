def retira_pontuacao(frase):
    '''função que retorna uma frase sem os caracteres de pontuação (travessão, vírgula, dois pontos, ponto e vírgula,
    e a pontuação de encerramento da frase), os substituindo por um espaço em branco.
    string -> string'''
    travessao = str.replace(frase, '-', ';')
    virgula = str.replace(travessao, ',', ';')
    doispontos = str.replace(virgula, ':', ';')
    pontoevirgula = str.replace(doispontos, ';', '')
    if pontoevirgula[len] == ' ':
        return pontoevirgula[0:len(doispontos)-2]
    else:
        return pontoevirgula[0:len(doispontos)-1]