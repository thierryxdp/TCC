def retira_pontuacao(frase):
    '''Função que, dada uma frase qualquer, retorna a mesma frase com os caracteres de pontuação substituídos por espaço.
str --> str'''
    frase_nova1 = frase.replace('.',' ')
    frase_nova2 = frase_nova1.replace('?',' ')
    frase_nova3 = frase_nova2.replace('!',' ')
    frase_nova4 = frase_nova3.replace(';',' ')
    frase_nova5 = frase_nova4.replace(',',' ')
    frase_nova6 = frase_nova5.replace(':',' ')
    frase_nova7 = frase_nova6.replace('-',' ')
    frase_nova8 = frase_nova7.replace('...',' ')
    return frase_nova8