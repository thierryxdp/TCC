"""A função ira remover "," "." "?" "!" "-"
str --> str """

def retira_pontuacao(x):
    A = x.replace(","," ")
    B = A.replace("."," ")
    C = B.replace("?"," ")
    D = C.replace("!"," ")
    E = D.replace("-"," ")
    return e