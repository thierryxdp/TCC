def retira_pontuacao(frase):
    '''Esta função retira todas as pontuações de uma frase,
    substituindo-as por espaço.
    str->str'''
    tira_ponto = str.replace(frase, '.', ' ')
    tira_virgula = str.replace(frase, ',', ' ')
    tira_doispontos = str.replace(frase, ':', ' ')
    tira_pontoevirgula = str.replace(frase, ';', ' ')