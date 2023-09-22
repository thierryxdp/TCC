def conta_frases(x):
    A = str.replace(".","'"), str.strip(x,"!"), str.strip(x,"?"), str.strip(x,"...")
	return len(A)