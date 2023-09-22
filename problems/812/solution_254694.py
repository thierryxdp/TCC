import string 
def retira_pontuacao(frase):
    s=frase
    punct=string.punctuation
    if c in punct:
        return s.replace(c,' ')