def inverte(x):
    return lista_strs(x)
def retira_pontuacao(x):
    a = str.replace(x,"-", " ")
    b = str.replace(a,":", " ")
    c = str.replace(b,".", " ")
    d = str.replace(c,";", " ")
    e = str.replace(d,"?", " ")
    f = str.replace(e,",", " ")
    g = str.replace(f,"!", " ")
    return g
def comp_f(x):
    return str.count(retira_pontuacao(x), " ") - str.count(retira_pontuacao(x), "  ")
def g_se(x):
    return str.replace(retira_pontuacao(x), "  ", " ")
def g_see(x):
    return str.replace(g_se(x), "  ", " ")
def lista_strs(x):
    return str.split(g_see(x)," ")