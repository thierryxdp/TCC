import string 
def retira_pontuacao(frase):
    s=frase
    x=string.punctuation
    a= ('!', '?', '-', ':', ';' '.', ',')
    for a in x:
        return s.replace(a,' ')
    else:
        return s.replace(a,' ')