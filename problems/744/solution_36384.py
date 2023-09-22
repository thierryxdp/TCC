def hashtag(s):
    """dada uma strign como parametro, retorna a mesma com uma # no inicio, meio e fim;
    str -> str"""
    a=len(s)
    b=a//2
    s=list(s)
    s.append("#")
    s.insert(0, "#")
    s.insert(b+1, "#")
    s="".join(s)
    return s