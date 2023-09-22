"""A função ira remover "," "." "?" "!" "-"
str --> str """

def retira_pontuacao(x):
    a = x.reaplace(","," ")
    b = a.reaplace("."," ")
    c = b.reaplace("?"," ")
    d = c.reaplace("!"," ")
    e = d.reaplace("-"," ")