def bsetor(x,y):
    a =[]
    for b in x:
        l=[]
        if b[2]==y:
            l.append(b[0])
            l.append(b[1])
            l.append(b[3])
        a.append(l)
    if len(a)!=0:
        return a
    else:
        return "nenhum registro encontrado"