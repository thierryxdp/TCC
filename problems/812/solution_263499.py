def inverte(frase):
    '''funcao que recebe uma frase, inverte a frase, retira pontuação e maiusculas
    str -> str'''
    frase1 = str.lower(frase)
    return frase1

def retira_pontuacao(frase):

    frase1 = str.replace(frase, ',', ' ')
    frase2 = str.replace(frase1,'.',' ')
    frase3 = str.replace(frase2,':',' ')
    frase4 = str.replace(frase3,';',' ')
    frase5 = str.replace(frase4,'!',' ')
    fraseFinal = str.replace(frase5,'?',' ')

    return fraseFinal