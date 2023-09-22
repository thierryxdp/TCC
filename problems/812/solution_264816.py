def retira_pontuacao(frase):
    '''função que dada uma frase como entrada, retorna a
    frase com todos os carácteres de pontuação substituídos
    por espaço
    string->string'''
    frase_substituida = frase.replace('?',' ')
    return frase_substituida