def inverte(x):
    def lista_final(x):
        r=[]
        j=0
        for i in x:
            j=j+1
            return list.append(r,x[comp_f(x)-j])
		return r
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