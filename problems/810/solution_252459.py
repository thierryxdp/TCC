def retira_pontuacao(frase):
    """Dada uma frase com pontuação, retorna a mesma frase sem pontuação
    str->str"""
    y=frase.replace(",","")
    x=y.replace("-"," ")
    z=x.replace(";","")
    h=z.replace(":","")
    i=h.replace(".","")
    j=i.replace("!","")
    k=j.replace("?","")
    return k

def inverte(fras):
    """Dada uma frase, retorna a mesma sem sinais de pontuação, apenas com letras minusculas e na ordem inversa
    str->str"""
    a=[fras]
    b=list.reverse[a]
    c=str(b)
    return c