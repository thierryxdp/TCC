import string
def retira_pontuacao(s):
    '''dada uma frase, a retorna com todos os caracteres de pontuação
    substituidos por espaço;
    string --> string'''
    for c in string.punctuation:
        s = s.replace(c, " ")
    return(s)