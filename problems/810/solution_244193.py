def retira_pontuacao(x):
    """função que vai receber uma frase e depois ela
    retorna a frase revertida"""
    x=str.replace(x,",", "")
    x=str.replace(x,".", "")
    x=str.replace(x,"-", " ")
    x=str.replace(x,"?", "")
    x=str.replace(x,":", "")
    x=str.replace(x,"!", "")
    x=str.replace(x,"...", "")
    x=str.replace(x,";", "")
    return x
def inverte(x):
    x=str.replace(x,"-"," ")
    a=str.slpit(x)
    b=str.lower(' '.join(list(reversed(a)))
    return retira_pontuacao (b)