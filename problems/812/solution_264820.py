def retira_pontuacao(frase):
    '''função que dada uma frase como entrada, retorna a
    frase com todos os carácteres de pontuação substituídos
    por espaço
    string->string'''
    pontuacao = '?' and '.'
    frase_substituida = frase.replace(pontuacao,' ')
    return frase_substituida