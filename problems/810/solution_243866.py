def retira_pontuacao(f):
    f=str.replace(f,",", " ")
    f=str.replace(f,".", " ")
    f=str.replace(f,"-", " ")
    f=str.replace(f,"?", " ")
    f=str.replace(f,":", " ")
    f=str.replace(f,"!", " ")
    f=str.replace(f,"...", " ")
    f=str.replace(f,";", " ")
    return f
def inverte(x):
    a=str.split(x)
    b=list.reverse(a)
    return str.join(b,'')