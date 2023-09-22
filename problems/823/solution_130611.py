def faltante(l):
    a=list(range(len(l)+3))[1:]
    b=list(range(l[-1]))[1:]
    if l in a:
        return len(l)+1
    else:
        return sum(b)-sum(l)