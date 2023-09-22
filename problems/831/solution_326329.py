def lingua_p(p):
    """recebe uma palavra e a "traduz" para a lingua do p
    str->str"""
    i=0
    for n in range(len(p)):
        if p[i] in "aeiouAEIOUáéíóúÁÉÍÓÚÊêãõÃÕàÀ":
            a=i+1
            p=p[:a]+'p'+p[i]+p[a:]
            i = i+3
        else:
            i = i+1
    return p