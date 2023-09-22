def lingua_p(palavra):
    P=palavra
    palavraa=list(palavra)
    y=[]
    x=['apa','epe','ipi','opo','upu']
    vogais=['a','e','i','o','u']
    z=P.replace('a',x[0])
    h=z.replace('e',x[1])
    j=h.replace('i',x[2])
    k=j.replace('o',x[3])
    l=k.replace('u',x[4])
    return z