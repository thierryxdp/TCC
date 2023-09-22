import string 
def retira_pontuacao(texto):
    out = texto.translate(str.maketrans('', '', string.punctuation)) 
    return out