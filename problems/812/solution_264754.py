def retira_pontuacao(frase):
    '''função que dada um frase de entrada retorna ela sem
    todos os caracteres de pontuação substituidos por
    espaços.
    str -> str'''
    frase_substituida = frase.replace(',',' ')
    frase_substituida = frase.replace('.',' ')
    frase_substituida = frase.replace('!',' ')
    return frase_substituida