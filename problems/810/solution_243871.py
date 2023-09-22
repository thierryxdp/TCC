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
    a=tr.join(reversed(x))
    
    return a