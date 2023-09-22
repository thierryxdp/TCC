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
    y=str.slpit(x)
    z=str.lower(' '.join(list(reversed(y)))
    return (z)