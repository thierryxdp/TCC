"""Retorna a frase inserida após substituir todos os caracteres de pontuação."""
def retira_pontuacao(x):
    a = str.replace(x,"-", " ")
    b = str.replace(a,":", " ")
    c = str.replace(b,".", " ")
    d = str.replace(c,";", " ")
    e = str.replace(d,"?", " ")
    f = str.replace(e,",", " ")
    g = str.replace(f,"!", " ")
    return g