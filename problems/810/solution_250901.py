def inverte(x):
    X = str.lower(x)
    A = X.replace("-"," ")
    B = A.replace(",","/")
    C = B.replace(".","/")
    D = C.replace("!","/")
    E = D.replace("?","/")
    F = E.replace("/","")
    G = F.split()
    H = G[::-1]
    I = str.join(" ",H)
    return I