def retira_pontuacao(frase):
    '''função que dada uma frase como entrada, retorna a
    frase com todos os carácteres de pontuação substituídos
    por espaço
    string->string'''
    var variavel = '?'
    var re = new regexp(variavel, ' ')
    frase_substituida = frase.replace(re,' ')
    return frase_substituida