def retira_pontuacao(frase):
    '''Funcao que dada uma frase, retira todos os caracteres de pontuacao e substitui por espaco'''
    s =  str.replace(frase,'.',' ').replace(',',' ').replace(':',' ').replace('-',' ').replace(';',' ').replace('!',' ').replace('?',' ')
    return s