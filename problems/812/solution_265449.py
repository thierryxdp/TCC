def retira_pontuacao(frase):
    '''função que dada uma frase retorna a mesma
    subtituindo as pontuações nela por espaços em branco
    string -> string'''
    return frase = frase.replace('.',' ').replace(';',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace('?',' ').replace('!',' ')