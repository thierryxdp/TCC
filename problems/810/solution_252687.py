def inverte(x):
    return len(lista_strs(x))
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
    return len(lista_strs(x))
def lista_strs(x):
    return str.split(retira_pontuacao(x))
def lista_final(x):
    r=[]
    for i in x:
        return list.append(r,x[comp_f(x)-i])