def conta_frases(x):
    A = x.replace("...","+")
	B = A.replace("!","+")
    C = B.replace("?","+")
    D = C.replace(".","+")
    E = D.split("+")
    return len(D)