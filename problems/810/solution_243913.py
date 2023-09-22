def retira_pontuacao(f):
    f=str.replace(f,",", "")
    f=str.replace(f,".", "")
    f=str.replace(f,"-", " ")
    f=str.replace(f,"?", "")
    f=str.replace(f,":", "")
    f=str.replace(f,"!", "")
    f=str.replace(f,"...", "")
    f=str.replace(f,";", "")
    return f
def inverte(f):
    f=str.replace(f,"-", " ")
    a=str.split(f)
    b=str.lower(' '.join(list(reversed(a))))
    return retira_pontuacao(b)