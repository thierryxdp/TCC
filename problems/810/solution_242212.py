def retira_pontuacao(frase):
    '''
       função que, dada uma frase, retorna a frase com todos
       os caracteres de pontuação substituídos por espaço
       str -> str
    '''
    frase1 = frase.replace('-',' ')
    frase2 = frase1.replace(',',' ')
    frase3 = frase2.replace(':',' ')
    frase4 = frase3.replace(';',' ')
    frase5 = frase4.replace('.',' ')
    frase6 = frase5.replace('?',' ')
    frase7 = frase6.replace('!',' ')
    frase8 = frase7.replace('...',' ')
    return frase8

def inverte(f_inicial):
    frase9 = print(frase8).lower()
    frase10 = frase9.split()
    return frase10.reverse()