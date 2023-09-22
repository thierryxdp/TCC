def inverte(x):
    """>.."""
    A= x.replace("."," ")
    B= A.replace("!"," ")
    C= B.replace(","," ")
    D= C.replace("-"," ")
    E= D.replace("?"," ")
    F= str.split(E)
    G= F[-1:-(len(F)+1):-1]
    H= str.join(" ",G)
    return str.lower(H)