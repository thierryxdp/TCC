import string 
def retira_pontuacao(frase):
    s=frase
    for a in string.ponctuation:
        return s.replace(a,' ')