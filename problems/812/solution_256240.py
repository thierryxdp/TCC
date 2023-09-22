import string
def retira_pontuação(frase):
    R = ""
    for i in frase:
       if i not in string.punctuation:
           R +=i 
    return  R