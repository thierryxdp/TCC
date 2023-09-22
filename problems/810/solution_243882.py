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
    b=' '.join(list(reversed(a)))
    return b