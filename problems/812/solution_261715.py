def retira_pontuacao(frase):
    '''calcule uma função que, dada uma frase,retorne a frase com todos os caracteres de pontuação substuídos por espaço.str-->str.'''
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' ')