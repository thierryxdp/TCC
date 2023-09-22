def retira_pontuacao(frase):
    '''Dada uma frase, retorna todos os caracteres de pontuação substituídos por espaços; string -> string'''
    return frase.split('...' ).split('.' ).split('?' ).split('!' ).split('-' ).split(' ' ).split(':' ).split(';' ).join