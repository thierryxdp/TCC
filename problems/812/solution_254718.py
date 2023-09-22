import string 
def retira_pontuacao(frase):
    s=frase
    x=string.punctuation
    for a in x:
        return s.replace(a,' ')
    for b in x:
        return s.replace(b,' ')