def retira_pontuacao(frase):
    '''função que dada uma frase, retorna ela onde todos os caracteres da pontuação e substitui por espaço;
    str -> str'''
    frase1 = frase.replace('-',' ')
    frase2 = frase1.replace(',',' ')
    frase3 = frase2.replace(':',' ')
    frase4 = frase3.replace(';',' ')
    frase5 = frase4.replace('.',' ')
    return frase5