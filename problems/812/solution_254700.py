import string 
def retira_pontuacao(frase):
    s=frase
    a=string.punctuation
    return s.replace(a,' ')