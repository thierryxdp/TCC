import string 
def retira_pontuacao(frase):
    s=frase
    x=string.punctuation
    for a in x:
        if a in len(s):
            return s.replace(a,' ')