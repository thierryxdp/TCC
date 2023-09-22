def lingua_p(palavra):
    P=palavra
    palavraa=list(palavra)
    y=[]
    x=['apa','epe','ipi','opo','upu']
    vogais=['a','e','i','o','u']
    a=P.replace('a',x[0])
    b=a.replace('á',x[0])
    d=b.replace('e',x[1])
    e=d.replace('é',x[1])
    f=e.replace('i',x[2])
    g=f.replace('í',x[2])
    h=g.replace('o',x[3])
    i=h.replace('ó',x[3])
    j=i.replace('u',x[4])
    k=j.replace('ú',x[4])
    return k