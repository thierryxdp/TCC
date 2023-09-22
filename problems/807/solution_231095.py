def conta_frases(x):
    A = x.replace("...","/")
	B = A.replace("!","/")
    C = B.replace("?","/")
    D = C.replace(".","/")
    E = C.split("/")
    return len(E)