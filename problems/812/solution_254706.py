import string 
def retira_pontuacao(frase):
    s=frase
    string.punctuation='-',',',':',';','.','!','?'
    x=string.punctuation
    for a in x:
        return s.replace(a,' ')