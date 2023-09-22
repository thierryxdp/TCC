def retira_pontuacao(f):
    """função que recebe uma frase e retorna a frase revertirda: str->str"""
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