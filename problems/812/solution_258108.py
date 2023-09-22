def retira_pontuacao(frase):
    '''A partir da frase de entrada retorna-a sem pontuacao(as marcas de
    pontuacao sao substituidas por espaco)
    str -> str'''
    ponto = str.replace(frase,'.',' ')
    virgula = str.replace(ponto,',',' ')
    doispontos = str.replace(virgula,':',' ')
    pontovirgula = str.replace(doispontos,';',' ')
    travessao = str.replace(pontovirgula,'—',' ')
    interrogacao = str.replace(travessao,'?',' ')
    exclamacao = str.replace(interrogacao,'!',' ')
    return exclamacao