import string 
def retira_pontuacao(frase):
    s=frase
    string.punctuation='-',',',':',';','.','!','?'
    x=string.ponctuation
    for a in x:
        return s.replace(a,' ')