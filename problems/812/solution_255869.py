def retira_pontuacao(frase):
    '''Função que formata um dado texto retirando todos os caracteres de pontuação e colocando um espaço no lugar.
    str -> str'''
    frase = frase.replace('.',' ').replace('?',' ').replace('!',' ').replace(';',' ').replace(':',' ').replace(',',' ').replace('-',' ')
    return frase