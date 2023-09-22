def inverte(x):
    A = x.replace("-","/")
    B = A.replace(",","/")
    C = B.replace(".","/")
    D = C.replace("!","/")
    E = D.replace("?","/")
    F = E.split("/")
    G = str.split(F)
    return G