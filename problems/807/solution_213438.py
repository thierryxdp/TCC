def conta_frases(frase):
    """essa funçao recebe um texto, conta quantas frase ele tem"""
    def conta_frases(frase):
    a=frase.replace(","," ")
    b=a.replace("!",",")
    c=b.replace("?",",")
    d=c.replace("-",",")
    e=d.replace(":",",")
    f=e.replace("...",".")
    g=f.replace(".",",")
    h=g.replace(", ''",".")
    return len(h.split(","))