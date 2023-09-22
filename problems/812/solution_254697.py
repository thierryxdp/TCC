import string 
def retira_pontuacao(frase):
    s=frase
    punct=string.punctuation
    for x in punct:
        return s.replace(x,' ')