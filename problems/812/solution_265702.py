"""A função ira remover "," "." "?" "!" "-"
str --> str """

def retira_pontuacao(x):
    A = x.reaplace(","," ")
    B = A.reaplace("."," ")
    C = B.reaplace("?"," ")
    D = C.reaplace("!"," ")
    E = D.reaplace("-"," ")
    return e