def retira_pontuacao(frase):
    '''Esta função retira todas as pontuações de uma frase,
    substituindo-as por espaço.
    str->str'''
    if '.' in frase:
        tira_ponto = str.replace(frase, '.', ' ')
    if ',' in frase:
        tira_virgula = str.replace(frase, ',', ' ')
    if ':' in frase:
        tira_doispontos = str.replace(frase, ':', ' ')
    if ';' in frase:
        tira_pontoevirgula = str.replace(frase, ';', ' ')
    if '!' in frase:
        tira_exclamacao = str.replace(frase, '!', ' ')
    if '?' in frase:
        tira_interrogacao = str.replace(frase, '?', ' ')