def retira_pontuacao(frase):
    """Dada uma frase com pontuação, retorna a mesma frase sem pontuação
    str->str"""
    y=frase.replace(",","")
    x=y.replace("-","")
    z=x.replace(";","")
    h=z.replace(":","")
    i=h.replace(".","")
    return i