def retira_pontuacao(frase):

    frase1 = str.replace(frase, ',', ' ')
    frase2 = str.replace(frase1,'.',' ')
    frase3 = str.replace(frase2,':',' ')
    frase4 = str.replace(frase3,';',' ')
    frase5 = str.replace(frase4,'!',' ')
    frase6 = str.replace(frase5,'-',' ')
    fraseFinal = str.replace(frase6,'?',' ')

    return fraseFinal

def inverte(frase):
    '''funcao que recebe uma frase, inverte a frase, retira pontuação e maiusculas
    str -> str'''
    frase1 = str.lower(retira_pontuacao(frase))
    frase2 = str.split(frase1)
    frase3 = str.join(' ', list.reverse(frase2))
    return frase3