def retira_pontuacao(x):
    '''função recebe uma frase de entrada e retorna a frase sem a pontuação.
    string -> string'''
    x.replace(',', '')
    x.replace('.', '')
    x.replace('!', '')
    x.replace('?', '')
    x.replace('-', '')
    x.replace(';', '')
    x.replace(':', '')
    return x