def retira_pontuacao(frase):
    '''função que dada uma frase, retorna a mesma, porém com os caracteres de pontuação substituidos por espaço
       str -> str'''
    frase=frase.replace(',',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    return frase