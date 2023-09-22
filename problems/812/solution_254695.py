import string 
def retira_pontuacao(frase):
    s=frase
    punct=string.punctuation
    for c in punct:
        return s.replace(c,' ')