import string
def retira_pontuacao(frase):
    R = ""
    for i in frase:
       if i not in string.punctuation:
           R +=i 
    return  R