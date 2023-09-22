import string 
def retira_pontuacao(frase): 
    for i in frase: 
       if i in string.punctuation:
           R = frase.replace(i, " ")
    return R