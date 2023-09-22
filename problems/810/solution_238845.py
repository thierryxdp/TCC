def inverte(x):
    """>.."""
    A= x.replace("."," ")
    B= A.replace("!"," ")
    C= B.replace(","," ")
    D= C.replace("-"," ")
    E= D.replace("?"," ")
    F= str.split(E)
    return F[-1:-(len(F)+1):-1]