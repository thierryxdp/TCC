def conta_frases(frase):
    w=str.replace(frase," ","-")
    a=str.replace(w,"."," ")
    b=str.replace(a,"!"," ")
    c=str.replace(b,"?"," ")
    d=str.replace(c,"..."," ")
    e=str.split(d)

    return len(e)