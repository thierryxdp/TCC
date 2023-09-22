def inverte(x):
    A = x.replace("-"," ")
    B = A.replace(",","/")
    C = B.replace(".","/")
    D = C.replace("!","/")
    E = D.replace("?","/")
    F = E.replace("/","")
    G = F.split()
    H = G[::-1]
    return H