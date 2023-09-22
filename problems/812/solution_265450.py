def retira_pontuacao(frase):
    '''função que dada uma frase retorna a mesma
    subtituindo as pontuações nela por espaços em branco
    string -> string'''
    frase = frase.replace('.',' ').replace(';',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace('?',' ').replace('!',' ')
    return frase