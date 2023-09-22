def retira_pontuacao(frase):
    '''Função que retorna a frase com todos os caracteres de
    pontuação substituidos por espaço
    str -> str'''
    pontuacoes = ['-', ',', ':', ';', '.', '!', '?']
    for ponto in pontuacoes:
        str.replace(frase, ponto, ' ')
    return frase