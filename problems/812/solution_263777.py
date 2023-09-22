def retira_pontuacao(frase):
    '''Esta função retira todas as pontuações de uma frase,
    substituindo-as por espaço.
    str->str'''
    if '.' in frase:
        tira_ponto = str.replace(frase, '.', ' ')
    elif ',' in frase:
        tira_ponto = str.replace(frase, ',', ' ')
    elif ':' in frase:
        tira_ponto = str.replace(frase, ':', ' ')
    elif ';' in frase:
        tira_ponto = str.replace(frase, ';', ' ')
    elif '!' in frase:
        tira_ponto = str.replace(frase, '!', ' ')
    elif '?' in frase:
        tira_ponto = str.replace(frase, '?', ' ')
    return tira_ponto